"""
Advanced cross-validation strategies for model evaluation.

Provides various CV strategies beyond simple holdout validation.
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
from sklearn.model_selection import (
    KFold,
    StratifiedKFold,
    TimeSeriesSplit,
    cross_val_score,
    cross_validate,
)


def perform_k_fold_cv(
    model: Any,
    X: pd.DataFrame,
    y: pd.Series,
    n_folds: int = 5,
    stratified: bool = True,
    metrics: Optional[List[str]] = None,
    seed: int = 42
) -> Dict[str, Any]:
    """
    Perform k-fold cross-validation.
    
    Args:
        model: Model to evaluate
        X: Features
        y: Labels
        n_folds: Number of folds
        stratified: Use stratified splits
        metrics: List of metrics to compute
        seed: Random seed
    
    Returns:
        Dictionary with CV results
    """
    if metrics is None:
        metrics = ["accuracy", "precision_weighted", "recall_weighted", "f1_weighted"]
    
    # Create CV splitter
    if stratified and len(np.unique(y)) < len(y):
        cv = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=seed)
    else:
        cv = KFold(n_splits=n_folds, shuffle=True, random_state=seed)
    
    print(f"Running {n_folds}-fold cross-validation...")
    
    # Perform cross-validation
    cv_results = cross_validate(
        model, X, y,
        cv=cv,
        scoring=metrics,
        return_train_score=True,
        return_estimator=True
    )
    
    # Compute statistics
    results = {
        "n_folds": n_folds,
        "stratified": stratified,
        "metrics": {}
    }
    
    for metric in metrics:
        test_scores = cv_results[f"test_{metric}"]
        train_scores = cv_results[f"train_{metric}"]
        
        results["metrics"][metric] = {
            "test_mean": float(np.mean(test_scores)),
            "test_std": float(np.std(test_scores)),
            "test_scores": [float(s) for s in test_scores],
            "train_mean": float(np.mean(train_scores)),
            "train_std": float(np.std(train_scores)),
            "train_scores": [float(s) for s in train_scores],
        }
        
        print(f"  {metric}: {np.mean(test_scores):.4f} ± {np.std(test_scores):.4f}")
    
    results["estimators"] = cv_results["estimator"]
    results["fit_times"] = [float(t) for t in cv_results["fit_time"]]
    results["score_times"] = [float(t) for t in cv_results["score_time"]]
    
    return results


def perform_time_series_cv(
    model: Any,
    X: pd.DataFrame,
    y: pd.Series,
    n_splits: int = 5,
    metrics: Optional[List[str]] = None,
    max_train_size: Optional[int] = None
) -> Dict[str, Any]:
    """
    Perform time series cross-validation.
    
    Args:
        model: Model to evaluate
        X: Features (time-ordered)
        y: Labels (time-ordered)
        n_splits: Number of splits
        metrics: List of metrics to compute
        max_train_size: Maximum size for training set
    
    Returns:
        Dictionary with CV results
    """
    if metrics is None:
        metrics = ["accuracy", "f1_weighted"]
    
    # Create time series CV splitter
    cv = TimeSeriesSplit(n_splits=n_splits, max_train_size=max_train_size)
    
    print(f"Running time series cross-validation with {n_splits} splits...")
    
    # Perform cross-validation
    cv_results = cross_validate(
        model, X, y,
        cv=cv,
        scoring=metrics,
        return_train_score=True
    )
    
    # Compute statistics
    results = {
        "n_splits": n_splits,
        "max_train_size": max_train_size,
        "metrics": {}
    }
    
    for metric in metrics:
        test_scores = cv_results[f"test_{metric}"]
        train_scores = cv_results[f"train_{metric}"]
        
        results["metrics"][metric] = {
            "test_mean": float(np.mean(test_scores)),
            "test_std": float(np.std(test_scores)),
            "test_scores": [float(s) for s in test_scores],
            "train_mean": float(np.mean(train_scores)),
            "train_std": float(np.std(train_scores)),
            "train_scores": [float(s) for s in train_scores],
        }
        
        print(f"  {metric}: {np.mean(test_scores):.4f} ± {np.std(test_scores):.4f}")
    
    return results


def nested_cross_validation(
    model: Any,
    param_grid: Dict[str, list],
    X: pd.DataFrame,
    y: pd.Series,
    outer_cv: int = 5,
    inner_cv: int = 3,
    scoring: str = "f1_weighted",
    seed: int = 42
) -> Dict[str, Any]:
    """
    Perform nested cross-validation for unbiased performance estimation.
    
    Args:
        model: Model to evaluate
        param_grid: Hyperparameter grid
        X: Features
        y: Labels
        outer_cv: Number of outer CV folds
        inner_cv: Number of inner CV folds
        scoring: Scoring metric
        seed: Random seed
    
    Returns:
        Dictionary with nested CV results
    """
    from sklearn.model_selection import GridSearchCV
    
    print(f"Running nested cross-validation ({outer_cv} outer, {inner_cv} inner folds)...")
    
    # Outer CV
    outer_cv_splitter = StratifiedKFold(
        n_splits=outer_cv,
        shuffle=True,
        random_state=seed
    )
    
    outer_scores = []
    best_params_list = []
    
    for fold_idx, (train_idx, test_idx) in enumerate(outer_cv_splitter.split(X, y)):
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
        
        # Inner CV for hyperparameter tuning
        inner_cv_splitter = StratifiedKFold(
            n_splits=inner_cv,
            shuffle=True,
            random_state=seed
        )
        
        grid_search = GridSearchCV(
            model,
            param_grid,
            cv=inner_cv_splitter,
            scoring=scoring,
            n_jobs=-1
        )
        
        grid_search.fit(X_train, y_train)
        
        # Evaluate on outer test fold
        score = grid_search.score(X_test, y_test)
        outer_scores.append(score)
        best_params_list.append(grid_search.best_params_)
        
        print(f"  Fold {fold_idx + 1}: {score:.4f} (params: {grid_search.best_params_})")
    
    results = {
        "outer_cv": outer_cv,
        "inner_cv": inner_cv,
        "scoring": scoring,
        "outer_scores": outer_scores,
        "mean_score": float(np.mean(outer_scores)),
        "std_score": float(np.std(outer_scores)),
        "best_params_per_fold": best_params_list,
    }
    
    print(f"\n✓ Nested CV score: {results['mean_score']:.4f} ± {results['std_score']:.4f}")
    
    return results


def leave_one_out_cv(
    model: Any,
    X: pd.DataFrame,
    y: pd.Series,
    metric: str = "accuracy"
) -> Dict[str, Any]:
    """
    Perform leave-one-out cross-validation.
    
    Note: Only use for small datasets (< 1000 samples).
    
    Args:
        model: Model to evaluate
        X: Features
        y: Labels
        metric: Metric to compute
    
    Returns:
        Dictionary with LOOCV results
    """
    from sklearn.model_selection import LeaveOneOut
    
    n_samples = len(X)
    
    if n_samples > 1000:
        print("⚠ Warning: LOOCV with > 1000 samples may be slow")
    
    print(f"Running leave-one-out cross-validation ({n_samples} iterations)...")
    
    loo = LeaveOneOut()
    scores = cross_val_score(model, X, y, cv=loo, scoring=metric)
    
    results = {
        "n_samples": n_samples,
        "metric": metric,
        "mean_score": float(np.mean(scores)),
        "std_score": float(np.std(scores)),
        "all_scores": [float(s) for s in scores],
    }
    
    print(f"✓ LOOCV {metric}: {results['mean_score']:.4f} ± {results['std_score']:.4f}")
    
    return results


def save_cv_results(results: Dict[str, Any], output_path: Path) -> None:
    """
    Save cross-validation results to file.
    
    Args:
        results: CV results dictionary
        output_path: Path to save results
    """
    # Remove non-serializable objects (estimators)
    results_copy = results.copy()
    if "estimators" in results_copy:
        del results_copy["estimators"]
    
    with open(output_path, "w") as f:
        json.dump(results_copy, f, indent=2)
    
    print(f"✓ Saved CV results to {output_path}")


def compare_cv_strategies(
    model: Any,
    X: pd.DataFrame,
    y: pd.Series,
    strategies: Optional[List[str]] = None,
    seed: int = 42
) -> Dict[str, Dict[str, Any]]:
    """
    Compare different cross-validation strategies.
    
    Args:
        model: Model to evaluate
        X: Features
        y: Labels
        strategies: List of strategies to compare
        seed: Random seed
    
    Returns:
        Dictionary with results for each strategy
    """
    if strategies is None:
        strategies = ["3-fold", "5-fold", "10-fold"]
    
    results = {}
    
    for strategy in strategies:
        if "fold" in strategy:
            n_folds = int(strategy.split("-")[0])
            results[strategy] = perform_k_fold_cv(
                model, X, y,
                n_folds=n_folds,
                seed=seed
            )
    
    # Print comparison
    print("\n=== CV Strategy Comparison ===")
    for strategy, result in results.items():
        f1_mean = result["metrics"]["f1_weighted"]["test_mean"]
        f1_std = result["metrics"]["f1_weighted"]["test_std"]
        print(f"{strategy}: F1 = {f1_mean:.4f} ± {f1_std:.4f}")
    
    return results
