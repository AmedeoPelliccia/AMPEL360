"""
MLflow integration for experiment tracking and model registry.

Provides centralized tracking of experiments, metrics, parameters, and models.
"""

import json
from pathlib import Path
from typing import Any, Dict, Optional

try:
    import mlflow
    import mlflow.sklearn
    MLFLOW_AVAILABLE = True
except ImportError:
    MLFLOW_AVAILABLE = False


class MLflowTracker:
    """Manage MLflow experiment tracking."""
    
    def __init__(
        self,
        tracking_uri: Optional[str] = None,
        experiment_name: str = "ca360_ml"
    ):
        """
        Initialize MLflow tracker.
        
        Args:
            tracking_uri: MLflow tracking server URI. Uses local if None.
            experiment_name: Name of the experiment
        """
        if not MLFLOW_AVAILABLE:
            raise ImportError(
                "MLflow not installed. Install with: pip install mlflow"
            )
        
        if tracking_uri:
            mlflow.set_tracking_uri(tracking_uri)
        
        self.experiment_name = experiment_name
        mlflow.set_experiment(experiment_name)
    
    def start_run(self, run_name: Optional[str] = None, tags: Optional[Dict[str, str]] = None):
        """
        Start a new MLflow run.
        
        Args:
            run_name: Name for the run
            tags: Tags to associate with the run
        
        Returns:
            MLflow run context manager
        """
        return mlflow.start_run(run_name=run_name, tags=tags)
    
    def log_params(self, params: Dict[str, Any]) -> None:
        """
        Log parameters to MLflow.
        
        Args:
            params: Dictionary of parameters to log
        """
        mlflow.log_params(params)
    
    def log_metrics(self, metrics: Dict[str, float], step: Optional[int] = None) -> None:
        """
        Log metrics to MLflow.
        
        Args:
            metrics: Dictionary of metrics to log
            step: Step number (for iterative training)
        """
        mlflow.log_metrics(metrics, step=step)
    
    def log_artifact(self, artifact_path: Path, artifact_type: Optional[str] = None) -> None:
        """
        Log an artifact to MLflow.
        
        Args:
            artifact_path: Path to artifact file
            artifact_type: Type of artifact (e.g., 'model', 'config')
        """
        mlflow.log_artifact(str(artifact_path), artifact_type)
    
    def log_model(
        self,
        model: Any,
        artifact_path: str = "model",
        registered_model_name: Optional[str] = None
    ) -> None:
        """
        Log a model to MLflow.
        
        Args:
            model: Model to log
            artifact_path: Path within run artifacts to store model
            registered_model_name: Name to register model under
        """
        mlflow.sklearn.log_model(
            model,
            artifact_path,
            registered_model_name=registered_model_name
        )
    
    def log_provenance(self, provenance: Dict[str, Any]) -> None:
        """
        Log provenance information to MLflow.
        
        Args:
            provenance: Provenance dictionary
        """
        # Log as tags
        tags = {
            "git_sha": provenance.get("git_sha", "unknown"),
            "dataset_id": provenance.get("dataset_id", "unknown"),
            "seed": str(provenance.get("seed", "")),
        }
        mlflow.set_tags(tags)
        
        # Log as artifact
        mlflow.log_dict(provenance, "provenance.json")
    
    def get_run_id(self) -> Optional[str]:
        """Get the current MLflow run ID."""
        active_run = mlflow.active_run()
        return active_run.info.run_id if active_run else None
    
    def end_run(self) -> None:
        """End the current MLflow run."""
        mlflow.end_run()


def track_training_run(
    run_name: str,
    config: Dict[str, Any],
    metrics: Dict[str, float],
    model: Any,
    provenance: Dict[str, Any],
    tracking_uri: Optional[str] = None,
    register_model: bool = False,
    model_name: Optional[str] = None
) -> str:
    """
    Track a complete training run in MLflow.
    
    Args:
        run_name: Name for the run
        config: Configuration dictionary
        metrics: Metrics dictionary
        model: Trained model
        provenance: Provenance dictionary
        tracking_uri: MLflow tracking server URI
        register_model: Whether to register model
        model_name: Name for registered model
    
    Returns:
        MLflow run ID
    """
    if not MLFLOW_AVAILABLE:
        print("⚠ MLflow not available. Skipping tracking.")
        return ""
    
    tracker = MLflowTracker(tracking_uri=tracking_uri)
    
    with tracker.start_run(run_name=run_name):
        # Log parameters from config
        training_params = config.get("training", {})
        hyperparameters = training_params.get("hyperparameters", {})
        tracker.log_params({
            "model_type": training_params.get("model_type"),
            "seed": training_params.get("seed"),
            **hyperparameters
        })
        
        # Log metrics
        tracker.log_metrics(metrics)
        
        # Log provenance
        tracker.log_provenance(provenance)
        
        # Log model
        registered_name = model_name if register_model else None
        tracker.log_model(model, registered_model_name=registered_name)
        
        run_id = tracker.get_run_id()
        print(f"✓ Tracked run in MLflow: {run_id}")
        
        return run_id


def compare_runs(
    run_ids: list,
    tracking_uri: Optional[str] = None
) -> Dict[str, Any]:
    """
    Compare multiple MLflow runs.
    
    Args:
        run_ids: List of MLflow run IDs to compare
        tracking_uri: MLflow tracking server URI
    
    Returns:
        Dictionary with comparison data
    """
    if not MLFLOW_AVAILABLE:
        print("⚠ MLflow not available.")
        return {}
    
    if tracking_uri:
        mlflow.set_tracking_uri(tracking_uri)
    
    client = mlflow.tracking.MlflowClient()
    
    comparison = {
        "runs": [],
        "metrics": {}
    }
    
    for run_id in run_ids:
        try:
            run = client.get_run(run_id)
            run_data = {
                "run_id": run_id,
                "run_name": run.data.tags.get("mlflow.runName", ""),
                "metrics": run.data.metrics,
                "params": run.data.params,
                "start_time": run.info.start_time,
                "end_time": run.info.end_time,
            }
            comparison["runs"].append(run_data)
            
            # Aggregate metrics
            for metric, value in run.data.metrics.items():
                if metric not in comparison["metrics"]:
                    comparison["metrics"][metric] = []
                comparison["metrics"][metric].append(value)
        except Exception as e:
            print(f"⚠ Failed to get run {run_id}: {e}")
    
    return comparison


def get_best_run(
    experiment_name: str,
    metric: str = "f1",
    tracking_uri: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """
    Get the best run from an experiment based on a metric.
    
    Args:
        experiment_name: Name of the experiment
        metric: Metric to optimize
        tracking_uri: MLflow tracking server URI
    
    Returns:
        Dictionary with best run information
    """
    if not MLFLOW_AVAILABLE:
        print("⚠ MLflow not available.")
        return None
    
    if tracking_uri:
        mlflow.set_tracking_uri(tracking_uri)
    
    client = mlflow.tracking.MlflowClient()
    
    try:
        experiment = client.get_experiment_by_name(experiment_name)
        if not experiment:
            print(f"⚠ Experiment '{experiment_name}' not found")
            return None
        
        runs = client.search_runs(
            experiment_ids=[experiment.experiment_id],
            order_by=[f"metrics.{metric} DESC"],
            max_results=1
        )
        
        if not runs:
            print(f"⚠ No runs found in experiment '{experiment_name}'")
            return None
        
        best_run = runs[0]
        return {
            "run_id": best_run.info.run_id,
            "run_name": best_run.data.tags.get("mlflow.runName", ""),
            "metrics": best_run.data.metrics,
            "params": best_run.data.params,
            "artifact_uri": best_run.info.artifact_uri,
        }
    except Exception as e:
        print(f"⚠ Failed to get best run: {e}")
        return None
