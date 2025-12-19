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


if __name__ == "__main__":
    cli()
