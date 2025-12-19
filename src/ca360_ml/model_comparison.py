"""
Model comparison dashboard for visualizing and comparing multiple models.

Provides interactive visualization and comparison of model performance.
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd

try:
    import plotly.graph_objects as go
    import plotly.express as px
    from plotly.subplots import make_subplots
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False


def create_metrics_comparison_chart(
    model_results: Dict[str, Dict[str, float]],
    metrics: Optional[List[str]] = None,
    output_path: Optional[Path] = None
) -> Optional[Any]:
    """
    Create a comparison chart for multiple models.
    
    Args:
        model_results: Dictionary mapping model names to their metrics
        metrics: List of metrics to compare
        output_path: Path to save chart HTML
    
    Returns:
        Plotly figure object
    """
    if not PLOTLY_AVAILABLE:
        print("✗ Plotly not available. Install with: pip install plotly")
        return None
    
    if metrics is None:
        metrics = ["accuracy", "precision", "recall", "f1"]
    
    # Prepare data
    df_data = []
    for model_name, model_metrics in model_results.items():
        for metric in metrics:
            if metric in model_metrics:
                df_data.append({
                    "Model": model_name,
                    "Metric": metric,
                    "Score": model_metrics[metric]
                })
    
    df = pd.DataFrame(df_data)
    
    # Create grouped bar chart
    fig = px.bar(
        df,
        x="Metric",
        y="Score",
        color="Model",
        barmode="group",
        title="Model Performance Comparison",
        labels={"Score": "Score (0-1)"},
        height=500
    )
    
    fig.update_layout(
        yaxis_range=[0, 1.1],
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    if output_path:
        fig.write_html(str(output_path))
        print(f"✓ Saved comparison chart to {output_path}")
    
    return fig


def create_confusion_matrix_comparison(
    model_cms: Dict[str, Any],
    class_names: Optional[List[str]] = None,
    output_path: Optional[Path] = None
) -> Optional[Any]:
    """
    Create comparison of confusion matrices for multiple models.
    
    Args:
        model_cms: Dictionary mapping model names to confusion matrices
        class_names: Names of classes
        output_path: Path to save chart HTML
    
    Returns:
        Plotly figure object
    """
    if not PLOTLY_AVAILABLE:
        print("✗ Plotly not available.")
        return None
    
    n_models = len(model_cms)
    cols = min(3, n_models)
    rows = (n_models + cols - 1) // cols
    
    fig = make_subplots(
        rows=rows,
        cols=cols,
        subplot_titles=list(model_cms.keys()),
        specs=[[{"type": "heatmap"}] * cols for _ in range(rows)]
    )
    
    for idx, (model_name, cm) in enumerate(model_cms.items()):
        row = idx // cols + 1
        col = idx % cols + 1
        
        # Normalize confusion matrix
        cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, None]
        
        heatmap = go.Heatmap(
            z=cm_normalized,
            x=class_names,
            y=class_names,
            colorscale="Blues",
            showscale=(idx == 0)
        )
        
        fig.add_trace(heatmap, row=row, col=col)
    
    fig.update_layout(
        title="Confusion Matrix Comparison",
        height=300 * rows,
        showlegend=False
    )
    
    if output_path:
        fig.write_html(str(output_path))
        print(f"✓ Saved confusion matrix comparison to {output_path}")
    
    return fig


def create_roc_curve_comparison(
    model_roc_data: Dict[str, Dict[str, Any]],
    output_path: Optional[Path] = None
) -> Optional[Any]:
    """
    Create ROC curve comparison for multiple models.
    
    Args:
        model_roc_data: Dictionary with model names and ROC data (fpr, tpr, auc)
        output_path: Path to save chart HTML
    
    Returns:
        Plotly figure object
    """
    if not PLOTLY_AVAILABLE:
        print("✗ Plotly not available.")
        return None
    
    fig = go.Figure()
    
    # Add ROC curves for each model
    for model_name, roc_data in model_roc_data.items():
        fig.add_trace(go.Scatter(
            x=roc_data["fpr"],
            y=roc_data["tpr"],
            mode="lines",
            name=f"{model_name} (AUC={roc_data['auc']:.3f})",
            line=dict(width=2)
        ))
    
    # Add diagonal reference line
    fig.add_trace(go.Scatter(
        x=[0, 1],
        y=[0, 1],
        mode="lines",
        name="Random",
        line=dict(dash="dash", color="gray")
    ))
    
    fig.update_layout(
        title="ROC Curve Comparison",
        xaxis_title="False Positive Rate",
        yaxis_title="True Positive Rate",
        yaxis=dict(scaleanchor="x", scaleratio=1),
        xaxis=dict(constrain="domain"),
        width=700,
        height=700
    )
    
    if output_path:
        fig.write_html(str(output_path))
        print(f"✓ Saved ROC curve comparison to {output_path}")
    
    return fig


def create_training_time_comparison(
    model_times: Dict[str, float],
    output_path: Optional[Path] = None
) -> Optional[Any]:
    """
    Create training time comparison chart.
    
    Args:
        model_times: Dictionary mapping model names to training times
        output_path: Path to save chart HTML
    
    Returns:
        Plotly figure object
    """
    if not PLOTLY_AVAILABLE:
        print("✗ Plotly not available.")
        return None
    
    df = pd.DataFrame([
        {"Model": name, "Time (s)": time}
        for name, time in model_times.items()
    ])
    
    fig = px.bar(
        df,
        x="Model",
        y="Time (s)",
        title="Training Time Comparison",
        color="Time (s)",
        color_continuous_scale="Viridis"
    )
    
    if output_path:
        fig.write_html(str(output_path))
        print(f"✓ Saved training time comparison to {output_path}")
    
    return fig


def generate_comparison_report(
    model_results: Dict[str, Dict[str, Any]],
    output_dir: Path
) -> None:
    """
    Generate comprehensive comparison report with all charts.
    
    Args:
        model_results: Dictionary with model names and their complete results
        output_dir: Directory to save report files
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("Generating model comparison report...")
    
    # Extract metrics
    metrics_data = {}
    for model_name, results in model_results.items():
        if "metrics" in results:
            metrics_data[model_name] = results["metrics"]
    
    # Create metrics comparison
    if metrics_data:
        create_metrics_comparison_chart(
            metrics_data,
            output_path=output_dir / "metrics_comparison.html"
        )
    
    # Extract training times
    time_data = {}
    for model_name, results in model_results.items():
        if "training_time" in results:
            time_data[model_name] = results["training_time"]
    
    # Create time comparison
    if time_data:
        create_training_time_comparison(
            time_data,
            output_path=output_dir / "time_comparison.html"
        )
    
    # Create summary table
    summary_df = pd.DataFrame([
        {
            "Model": name,
            **results.get("metrics", {}),
            "Training Time (s)": results.get("training_time", "N/A")
        }
        for name, results in model_results.items()
    ])
    
    summary_path = output_dir / "comparison_summary.csv"
    summary_df.to_csv(summary_path, index=False)
    print(f"✓ Saved comparison summary to {summary_path}")
    
    # Create markdown report
    markdown_report = generate_markdown_report(model_results)
    report_path = output_dir / "comparison_report.md"
    with open(report_path, "w", encoding="utf_8") as f:
        f.write(markdown_report)
    print(f"✓ Saved comparison report to {report_path}")


def generate_markdown_report(model_results: Dict[str, Dict[str, Any]]) -> str:
    """
    Generate markdown report for model comparison.
    
    Args:
        model_results: Dictionary with model results
    
    Returns:
        Markdown string
    """
    report = "# Model Comparison Report\n\n"
    report += f"**Number of models compared:** {len(model_results)}\n\n"
    
    # Summary table
    report += "## Performance Summary\n\n"
    report += "| Model | Accuracy | Precision | Recall | F1 | Training Time |\n"
    report += "|-------|----------|-----------|--------|----|--------------|\n"
    
    for model_name, results in model_results.items():
        metrics = results.get("metrics", {})
        time = results.get("training_time", "N/A")
        report += f"| {model_name} | "
        report += f"{metrics.get('accuracy', 'N/A'):.4f} | "
        report += f"{metrics.get('precision', 'N/A'):.4f} | "
        report += f"{metrics.get('recall', 'N/A'):.4f} | "
        report += f"{metrics.get('f1', 'N/A'):.4f} | "
        report += f"{time} |\n"
    
    # Best model
    report += "\n## Best Model\n\n"
    best_model = max(
        model_results.items(),
        key=lambda x: x[1].get("metrics", {}).get("f1", 0)
    )
    report += f"**{best_model[0]}** achieved the highest F1 score: "
    report += f"{best_model[1].get('metrics', {}).get('f1', 0):.4f}\n\n"
    
    # Visualizations
    report += "## Visualizations\n\n"
    report += "- [Metrics Comparison](metrics_comparison.html)\n"
    report += "- [Training Time Comparison](time_comparison.html)\n"
    report += "- [Detailed Results](comparison_summary.csv)\n"
    
    return report


def rank_models(
    model_results: Dict[str, Dict[str, Any]],
    primary_metric: str = "f1",
    secondary_metric: Optional[str] = "accuracy"
) -> List[Dict[str, Any]]:
    """
    Rank models by performance metrics.
    
    Args:
        model_results: Dictionary with model results
        primary_metric: Primary metric for ranking
        secondary_metric: Secondary metric for tie-breaking
    
    Returns:
        List of ranked models with scores
    """
    rankings = []
    
    for model_name, results in model_results.items():
        metrics = results.get("metrics", {})
        rankings.append({
            "model": model_name,
            "primary_score": metrics.get(primary_metric, 0),
            "secondary_score": metrics.get(secondary_metric, 0) if secondary_metric else 0,
            "all_metrics": metrics
        })
    
    # Sort by primary, then secondary metric
    rankings.sort(
        key=lambda x: (x["primary_score"], x["secondary_score"]),
        reverse=True
    )
    
    print(f"\n=== Model Rankings (by {primary_metric}) ===")
    for idx, rank in enumerate(rankings, 1):
        print(f"{idx}. {rank['model']}: {rank['primary_score']:.4f}")
    
    return rankings
