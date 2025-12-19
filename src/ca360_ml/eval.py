"""
Evaluation utilities for model assessment and validation gates.
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import joblib
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)


def compute_metrics(
    y_true: pd.Series,
    y_pred: pd.Series,
    y_proba: Optional[pd.Series] = None,
    metrics_list: Optional[List[str]] = None
) -> Dict[str, float]:
    """
    Compute evaluation metrics.
    
    Args:
        y_true: True labels
        y_pred: Predicted labels
        y_proba: Predicted probabilities (for ROC-AUC)
        metrics_list: List of metrics to compute
    
    Returns:
        Dictionary of metric name to value
    """
    if metrics_list is None:
        metrics_list = ["accuracy", "precision", "recall", "f1"]
    
    metrics = {}
    
    if "accuracy" in metrics_list:
        metrics["accuracy"] = float(accuracy_score(y_true, y_pred))
    
    if "precision" in metrics_list:
        metrics["precision"] = float(precision_score(y_true, y_pred, average="weighted", zero_division=0))
    
    if "recall" in metrics_list:
        metrics["recall"] = float(recall_score(y_true, y_pred, average="weighted", zero_division=0))
    
    if "f1" in metrics_list:
        metrics["f1"] = float(f1_score(y_true, y_pred, average="weighted", zero_division=0))
    
    if "roc_auc" in metrics_list and y_proba is not None:
        try:
            metrics["roc_auc"] = float(roc_auc_score(y_true, y_proba, average="weighted", multi_class="ovr"))
        except ValueError:
            # Skip if not applicable (e.g., single class)
            pass
    
    return metrics


def evaluate_model(
    model: Any,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    config: Dict[str, Any],
    run_dir: Path
) -> Dict[str, float]:
    """
    Evaluate model and save results.
    
    Args:
        model: Trained model
        X_test: Test features
        y_test: Test labels
        config: Evaluation configuration
        run_dir: Directory to save evaluation results
    
    Returns:
        Dictionary of metrics
    """
    eval_config = config.get("evaluation", {})
    
    print(f"Evaluating on {X_test.shape[0]} test samples...")
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Get probabilities if available
    y_proba = None
    if hasattr(model, "predict_proba"):
        y_proba_full = model.predict_proba(X_test)
        # For binary classification, use positive class probability
        if y_proba_full.shape[1] == 2:
            y_proba = y_proba_full[:, 1]
        else:
            y_proba = y_proba_full
    
    # Compute metrics
    metrics_list = eval_config.get("metrics", ["accuracy", "precision", "recall", "f1"])
    metrics = compute_metrics(y_test, y_pred, y_proba, metrics_list)
    
    print("\n=== Evaluation Metrics ===")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")
    
    # Save metrics
    metrics_path = run_dir / "metrics.json"
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"\nMetrics saved to: {metrics_path}")
    
    # Generate confusion matrix if requested
    if eval_config.get("generate_confusion_matrix", False):
        cm = confusion_matrix(y_test, y_pred)
        cm_path = run_dir / "confusion_matrix.csv"
        pd.DataFrame(cm).to_csv(cm_path, index=False)
        print(f"Confusion matrix saved to: {cm_path}")
    
    # Generate markdown report
    generate_report(metrics, run_dir, config)
    
    return metrics


def check_thresholds(
    metrics: Dict[str, float],
    thresholds: Dict[str, float]
) -> Tuple[bool, List[str]]:
    """
    Check if metrics meet threshold requirements.
    
    Args:
        metrics: Computed metrics
        thresholds: Required thresholds
    
    Returns:
        Tuple of (all_passed, list_of_failures)
    """
    failures = []
    
    for metric, threshold in thresholds.items():
        if metric in metrics:
            if metrics[metric] < threshold:
                failures.append(f"{metric}: {metrics[metric]:.4f} < {threshold:.4f}")
    
    return len(failures) == 0, failures


def check_regression(
    current_metrics: Dict[str, float],
    baseline_path: Path,
    tolerance: float = 0.02
) -> Tuple[bool, List[str]]:
    """
    Check for performance regression compared to baseline.
    
    Args:
        current_metrics: Current run metrics
        baseline_path: Path to baseline metrics JSON
        tolerance: Acceptable degradation tolerance
    
    Returns:
        Tuple of (no_regression, list_of_regressions)
    """
    if not baseline_path.exists():
        print(f"⚠ Baseline metrics not found: {baseline_path}")
        return True, []
    
    with open(baseline_path) as f:
        baseline_metrics = json.load(f)
    
    regressions = []
    
    for metric, baseline_value in baseline_metrics.items():
        if metric in current_metrics:
            current_value = current_metrics[metric]
            degradation = baseline_value - current_value
            
            if degradation > tolerance:
                regressions.append(
                    f"{metric}: {current_value:.4f} vs baseline {baseline_value:.4f} "
                    f"(degradation: {degradation:.4f})"
                )
    
    return len(regressions) == 0, regressions


def evaluation_gate(
    run_dir: Path,
    config: Dict[str, Any]
) -> bool:
    """
    Run evaluation gates and determine if run passes.
    
    Args:
        run_dir: Run directory with metrics
        config: Evaluation configuration
    
    Returns:
        True if all gates pass, False otherwise
    """
    eval_config = config.get("evaluation", {})
    
    # Load metrics
    metrics_path = run_dir / "metrics.json"
    if not metrics_path.exists():
        print("❌ Metrics file not found")
        return False
    
    with open(metrics_path) as f:
        metrics = json.load(f)
    
    print("\n=== Evaluation Gates ===")
    
    # Check thresholds
    thresholds = eval_config.get("thresholds", {})
    if thresholds:
        passed, failures = check_thresholds(metrics, thresholds)
        if passed:
            print("✓ All threshold gates passed")
        else:
            print("❌ Threshold gate failures:")
            for failure in failures:
                print(f"  - {failure}")
            return False
    
    # Check regression
    regression_config = eval_config.get("regression_check", {})
    if regression_config.get("enabled", False):
        baseline_path = Path(regression_config.get("baseline_metrics_path", "reports/baseline_metrics.json"))
        tolerance = regression_config.get("tolerance", 0.02)
        
        no_regression, regressions = check_regression(metrics, baseline_path, tolerance)
        if no_regression:
            print("✓ No performance regression detected")
        else:
            print("❌ Performance regressions detected:")
            for regression in regressions:
                print(f"  - {regression}")
            return False
    
    print("\n✓ All evaluation gates PASSED")
    return True


def generate_report(
    metrics: Dict[str, float],
    run_dir: Path,
    config: Dict[str, Any]
) -> None:
    """
    Generate markdown evaluation report.
    
    Args:
        metrics: Computed metrics
        run_dir: Run directory
        config: Configuration
    """
    report_path = run_dir / "report.md"
    
    with open(report_path, "w", encoding="utf_8") as f:
        f.write("# Evaluation Report\n\n")
        f.write(f"**Run ID:** {run_dir.name}\n\n")
        
        f.write("## Metrics\n\n")
        f.write("| Metric | Value |\n")
        f.write("|--------|-------|\n")
        for metric, value in metrics.items():
            f.write(f"| {metric} | {value:.4f} |\n")
        
        f.write("\n## Threshold Gates\n\n")
        thresholds = config.get("evaluation", {}).get("thresholds", {})
        if thresholds:
            passed, failures = check_thresholds(metrics, thresholds)
            if passed:
                f.write("✓ All threshold gates passed\n")
            else:
                f.write("❌ Threshold gate failures:\n\n")
                for failure in failures:
                    f.write(f"- {failure}\n")
    
    print(f"Report saved to: {report_path}")
