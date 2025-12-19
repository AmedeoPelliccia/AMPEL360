"""
CLI interface for CA360 ML Pipeline.

Commands:
- dataset: Dataset operations (validate, build)
- train: Train models
- eval: Evaluate models
- package: Package models for deployment
"""

import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Optional

import click
import yaml

from . import __version__
from .data import (
    load_dataset_from_manifest,
    preprocess_data,
    split_dataset,
    validate_dataset_manifest,
)
from .eval import evaluate_model, evaluation_gate
from .package import package_model
from .reproducibility import create_provenance_manifest
from .train import save_config, train_model


def load_config(config_path: Path) -> dict:
    """Load YAML configuration file."""
    with open(config_path) as f:
        return yaml.safe_load(f)


def get_latest_run_dir() -> Optional[Path]:
    """Get the most recent run directory."""
    runs_dir = Path("runs")
    if not runs_dir.exists():
        return None
    
    run_dirs = [d for d in runs_dir.iterdir() if d.is_dir()]
    if not run_dirs:
        return None
    
    return max(run_dirs, key=lambda d: d.stat().st_mtime)


@click.group()
@click.version_option(version=__version__)
def cli():
    """CA360 ML Pipeline - Baseline Training Pipeline for AMPEL360."""
    pass


@cli.group()
def dataset():
    """Dataset operations."""
    pass


@dataset.command()
@click.option("--manifest", type=click.Path(exists=True), required=True, help="Path to dataset manifest")
def validate(manifest: str):
    """Validate dataset manifest."""
    manifest_path = Path(manifest)
    click.echo(f"Validating dataset manifest: {manifest_path}")
    
    if validate_dataset_manifest(manifest_path):
        click.echo("✓ Dataset manifest is valid")
    else:
        click.echo("❌ Dataset manifest validation failed", err=True)
        raise click.Abort()


@cli.command()
@click.option("--config", type=click.Path(exists=True), required=True, help="Baseline configuration file")
@click.option("--dataset-manifest", type=click.Path(exists=True), required=True, help="Dataset manifest file")
@click.option("--use-sample", is_flag=True, help="Use sample dataset for CI")
@click.option("--run-id", type=str, help="Custom run ID (auto-generated if not provided)")
def train(config: str, dataset_manifest: str, use_sample: bool, run_id: Optional[str]):
    """Train baseline model."""
    config_path = Path(config)
    manifest_path = Path(dataset_manifest)
    
    click.echo("=== CA360 ML Pipeline - Training ===")
    click.echo(f"Config: {config_path}")
    click.echo(f"Dataset manifest: {manifest_path}")
    
    # Load configuration
    full_config = load_config(config_path)
    
    # Generate run ID
    if run_id is None:
        run_id = f"run_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}"
    
    click.echo(f"Run ID: {run_id}")
    
    # Create run directory
    run_dir = Path("runs") / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    click.echo(f"Run directory: {run_dir}")
    
    # Validate dataset manifest
    click.echo("\n--- Validating dataset manifest ---")
    if not validate_dataset_manifest(manifest_path):
        click.echo("❌ Dataset manifest validation failed", err=True)
        raise click.Abort()
    
    # Load dataset
    click.echo("\n--- Loading dataset ---")
    sample_path = None
    if use_sample:
        sample_path = Path(full_config.get("baseline", {}).get("run", {}).get("sample_path", "data/samples/ci_sample.csv"))
    
    df, manifest = load_dataset_from_manifest(manifest_path, use_sample, sample_path)
    
    # Save dataset manifest to run directory
    shutil.copy2(manifest_path, run_dir / "dataset_manifest.json")
    
    # Split dataset
    click.echo("\n--- Splitting dataset ---")
    dataset_config = manifest  # Use manifest splits
    X_train, X_val, X_test, y_train, y_val, y_test = split_dataset(df, dataset_config)
    
    # Preprocess data
    click.echo("\n--- Preprocessing data ---")
    X_train, X_val, X_test = preprocess_data(X_train, X_val, X_test, full_config)
    
    # Save configuration
    click.echo("\n--- Saving configuration ---")
    save_config(full_config, run_dir)
    
    # Train model
    click.echo("\n--- Training model ---")
    model = train_model(X_train, y_train, X_val, y_val, full_config, run_dir)
    
    # Evaluate model
    click.echo("\n--- Evaluating model ---")
    metrics = evaluate_model(model, X_test, y_test, full_config, run_dir)
    
    # Create provenance manifest
    click.echo("\n--- Creating provenance manifest ---")
    seed = full_config.get("training", {}).get("seed", 42)
    provenance = create_provenance_manifest(
        run_id=run_id,
        dataset_manifest_path=manifest_path,
        config=full_config,
        seed=seed,
        metrics=metrics
    )
    
    provenance_path = run_dir / "provenance.json"
    with open(provenance_path, "w") as f:
        json.dump(provenance, f, indent=2)
    click.echo(f"Provenance manifest saved: {provenance_path}")
    
    click.echo(f"\n✓ Training complete: {run_dir}")


@cli.command()
@click.option("--run-id", type=str, help="Run ID to evaluate")
@click.option("--last-run", is_flag=True, help="Evaluate the most recent run")
@click.option("--config", type=click.Path(exists=True), required=True, help="Evaluation configuration")
def eval(run_id: Optional[str], last_run: bool, config: str):
    """Evaluate model from a run."""
    if last_run:
        run_dir = get_latest_run_dir()
        if run_dir is None:
            click.echo("❌ No runs found", err=True)
            raise click.Abort()
    elif run_id:
        run_dir = Path("runs") / run_id
        if not run_dir.exists():
            click.echo(f"❌ Run not found: {run_dir}", err=True)
            raise click.Abort()
    else:
        click.echo("❌ Must specify --run-id or --last-run", err=True)
        raise click.Abort()
    
    click.echo(f"=== Evaluating run: {run_dir.name} ===")
    
    # Metrics should already be computed during training
    metrics_path = run_dir / "metrics.json"
    if metrics_path.exists():
        with open(metrics_path) as f:
            metrics = json.load(f)
        
        click.echo("\nMetrics:")
        for metric, value in metrics.items():
            click.echo(f"  {metric}: {value:.4f}")
    else:
        click.echo("⚠ No metrics found (run 'train' first)")


@cli.group()
def eval_gate():
    """Evaluation gate commands."""
    pass


@eval_gate.command(name="check")
@click.option("--run-id", type=str, help="Run ID to check")
@click.option("--last-run", is_flag=True, help="Check the most recent run")
@click.option("--config", type=click.Path(exists=True), required=True, help="Evaluation configuration")
def gate_check(run_id: Optional[str], last_run: bool, config: str):
    """Check evaluation gates for a run."""
    if last_run:
        run_dir = get_latest_run_dir()
        if run_dir is None:
            click.echo("❌ No runs found", err=True)
            raise click.Abort()
    elif run_id:
        run_dir = Path("runs") / run_id
        if not run_dir.exists():
            click.echo(f"❌ Run not found: {run_dir}", err=True)
            raise click.Abort()
    else:
        click.echo("❌ Must specify --run-id or --last-run", err=True)
        raise click.Abort()
    
    click.echo(f"=== Checking evaluation gates: {run_dir.name} ===")
    
    # Load configuration
    full_config = load_config(Path(config))
    
    # Run evaluation gates
    if evaluation_gate(run_dir, full_config):
        click.echo("\n✓ All evaluation gates PASSED")
    else:
        click.echo("\n❌ Evaluation gates FAILED", err=True)
        raise click.Abort()


@cli.command()
@click.option("--run-id", type=str, help="Run ID to package")
@click.option("--last-run", is_flag=True, help="Package the most recent run")
def package(run_id: Optional[str], last_run: bool):
    """Package model for deployment."""
    if last_run:
        run_dir = get_latest_run_dir()
        if run_dir is None:
            click.echo("❌ No runs found", err=True)
            raise click.Abort()
        run_id = run_dir.name
    elif run_id:
        run_dir = Path("runs") / run_id
        if not run_dir.exists():
            click.echo(f"❌ Run not found: {run_dir}", err=True)
            raise click.Abort()
    else:
        click.echo("❌ Must specify --run-id or --last-run", err=True)
        raise click.Abort()
    
    click.echo(f"=== Packaging model: {run_id} ===")
    
    model_registry_dir = Path("models/registry")
    package_dir = package_model(run_dir, model_registry_dir, run_id)
    
    click.echo(f"\n✓ Model packaged: {package_dir}")


# Register the eval_gate group properly
cli.add_command(eval_gate, name="gate")


# ============================================================================
# Enhanced Features Commands
# ============================================================================

@cli.command()
@click.option("--model-path", type=click.Path(exists=True), required=True, help="Path to trained model")
@click.option("--n-features", type=int, required=True, help="Number of input features")
@click.option("--output", type=click.Path(), required=True, help="Output path for ONNX model")
def export_onnx(model_path: str, n_features: int, output: str):
    """Export trained model to ONNX format."""
    try:
        from .onnx_export import export_sklearn_to_onnx, validate_onnx_model
        import joblib
    except ImportError:
        click.echo("❌ ONNX dependencies not installed. Install with: pip install ca360-ml[onnx]", err=True)
        raise click.Abort()
    
    click.echo("=== Exporting model to ONNX ===")
    
    # Load model
    model = joblib.load(model_path)
    
    # Export to ONNX
    onnx_path = export_sklearn_to_onnx(
        model,
        n_features=n_features,
        output_path=Path(output)
    )
    
    if onnx_path:
        # Validate
        if validate_onnx_model(onnx_path):
            click.echo(f"✓ Model exported and validated: {onnx_path}")
        else:
            click.echo("⚠ Model exported but validation failed", err=True)
    else:
        click.echo("❌ Export failed", err=True)
        raise click.Abort()


@cli.command()
@click.option("--config", type=click.Path(exists=True), required=True, help="Training configuration")
@click.option("--dataset-manifest", type=click.Path(exists=True), required=True, help="Dataset manifest")
@click.option("--n-trials", type=int, default=50, help="Number of tuning trials")
@click.option("--use-sample", is_flag=True, help="Use sample dataset")
def tune(config: str, dataset_manifest: str, n_trials: int, use_sample: bool):
    """Tune hyperparameters with Optuna."""
    try:
        from .hyperparameter_tuning import tune_random_forest
    except ImportError:
        click.echo("❌ Tuning dependencies not installed. Install with: pip install ca360-ml[tuning]", err=True)
        raise click.Abort()
    
    click.echo("=== Hyperparameter Tuning ===")
    click.echo(f"Trials: {n_trials}")
    
    # Load configuration and dataset
    full_config = load_config(Path(config))
    manifest_path = Path(dataset_manifest)
    
    sample_path = None
    if use_sample:
        sample_path = Path(full_config.get("baseline", {}).get("run", {}).get("sample_path", "data/samples/ci_sample.csv"))
    
    df, manifest = load_dataset_from_manifest(manifest_path, use_sample, sample_path)
    X_train, X_val, X_test, y_train, y_val, y_test = split_dataset(df, manifest)
    
    # Run tuning
    results = tune_random_forest(X_train, y_train, n_trials=n_trials)
    
    # Save results
    tuning_dir = Path("runs/tuning")
    tuning_dir.mkdir(parents=True, exist_ok=True)
    
    results_path = tuning_dir / f"tuning_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    
    click.echo(f"\n✓ Tuning complete. Results saved to: {results_path}")


@cli.command()
@click.option("--config", type=click.Path(exists=True), required=True, help="Training configuration")
@click.option("--dataset-manifest", type=click.Path(exists=True), required=True, help="Dataset manifest")
@click.option("--n-folds", type=int, default=5, help="Number of CV folds")
@click.option("--use-sample", is_flag=True, help="Use sample dataset")
def cross_validate(config: str, dataset_manifest: str, n_folds: int, use_sample: bool):
    """Perform cross-validation."""
    try:
        from .cross_validation import perform_k_fold_cv
        from .train import create_model
    except ImportError:
        click.echo("❌ Dependencies not installed", err=True)
        raise click.Abort()
    
    click.echo("=== Cross-Validation ===")
    click.echo(f"Folds: {n_folds}")
    
    # Load configuration and dataset
    full_config = load_config(Path(config))
    manifest_path = Path(dataset_manifest)
    
    sample_path = None
    if use_sample:
        sample_path = Path(full_config.get("baseline", {}).get("run", {}).get("sample_path", "data/samples/ci_sample.csv"))
    
    df, manifest = load_dataset_from_manifest(manifest_path, use_sample, sample_path)
    X_train, _, _, y_train, _, _ = split_dataset(df, manifest)
    
    # Create model
    training_config = full_config.get("training", {})
    model_type = training_config.get("model_type", "sklearn_random_forest")
    hyperparameters = training_config.get("hyperparameters", {})
    model = create_model(model_type, hyperparameters)
    
    # Run CV
    results = perform_k_fold_cv(model, X_train, y_train, n_folds=n_folds)
    
    # Save results
    cv_dir = Path("runs/cv")
    cv_dir.mkdir(parents=True, exist_ok=True)
    
    from .cross_validation import save_cv_results
    results_path = cv_dir / f"cv_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
    save_cv_results(results, results_path)
    
    click.echo("\n✓ Cross-validation complete")


@cli.command()
@click.option("--run-ids", multiple=True, required=True, help="Run IDs to compare")
@click.option("--output-dir", type=click.Path(), default="reports/comparison", help="Output directory")
def compare(run_ids: tuple, output_dir: str):
    """Compare multiple model runs."""
    try:
        from .model_comparison import generate_comparison_report
    except ImportError:
        click.echo("❌ Comparison dependencies not installed. Install with: pip install ca360-ml[all]", err=True)
        raise click.Abort()
    
    click.echo("=== Model Comparison ===")
    click.echo(f"Comparing {len(run_ids)} models")
    
    model_results = {}
    
    for run_id in run_ids:
        run_dir = Path("runs") / run_id
        if not run_dir.exists():
            click.echo(f"⚠ Run not found: {run_id}")
            continue
        
        # Load metrics
        metrics_path = run_dir / "metrics.json"
        if metrics_path.exists():
            with open(metrics_path) as f:
                metrics = json.load(f)
            
            # Load training metadata
            metadata_path = run_dir / "training_metadata.json"
            training_time = None
            if metadata_path.exists():
                with open(metadata_path) as f:
                    metadata = json.load(f)
                    training_time = metadata.get("training_time_seconds")
            
            model_results[run_id] = {
                "metrics": metrics,
                "training_time": training_time
            }
    
    if not model_results:
        click.echo("❌ No valid runs found to compare", err=True)
        raise click.Abort()
    
    # Generate report
    output_path = Path(output_dir)
    generate_comparison_report(model_results, output_path)
    
    click.echo(f"\n✓ Comparison report generated: {output_path}")


@cli.group()
def mlflow():
    """MLflow integration commands."""
    pass


@mlflow.command(name="track")
@click.option("--run-id", type=str, required=True, help="Run ID to track in MLflow")
@click.option("--tracking-uri", type=str, help="MLflow tracking URI")
@click.option("--experiment-name", type=str, default="ca360_ml", help="Experiment name")
def mlflow_track(run_id: str, tracking_uri: Optional[str], experiment_name: str):
    """Track a run in MLflow."""
    try:
        from .mlflow_integration import track_training_run
        import joblib
    except ImportError:
        click.echo("❌ MLflow not installed. Install with: pip install ca360-ml[mlflow]", err=True)
        raise click.Abort()
    
    run_dir = Path("runs") / run_id
    if not run_dir.exists():
        click.echo(f"❌ Run not found: {run_dir}", err=True)
        raise click.Abort()
    
    click.echo(f"=== Tracking run in MLflow: {run_id} ===")
    
    # Load artifacts
    with open(run_dir / "config_resolved.json") as f:
        config = json.load(f)
    
    with open(run_dir / "metrics.json") as f:
        metrics = json.load(f)
    
    with open(run_dir / "provenance.json") as f:
        provenance = json.load(f)
    
    model = joblib.load(run_dir / "model.joblib")
    
    # Track in MLflow
    mlflow_run_id = track_training_run(
        run_name=run_id,
        config=config,
        metrics=metrics,
        model=model,
        provenance=provenance,
        tracking_uri=tracking_uri
    )
    
    click.echo(f"✓ Tracked in MLflow with run ID: {mlflow_run_id}")


# Register MLflow group
cli.add_command(mlflow)


if __name__ == "__main__":
    cli()
