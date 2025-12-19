"""
Packaging utilities for creating release-ready model artifacts.
"""

import json
import shutil
from pathlib import Path
from typing import Any, Dict

import joblib


def package_model(
    run_dir: Path,
    model_registry_dir: Path,
    run_id: str
) -> Path:
    """
    Package model with all artifacts for release.
    
    Args:
        run_dir: Run directory with all artifacts
        model_registry_dir: Target model registry directory
        run_id: Run identifier
    
    Returns:
        Path to packaged model directory
    """
    # Create package directory
    package_dir = model_registry_dir / run_id
    package_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Packaging model to: {package_dir}")
    
    # Copy model artifact
    model_src = run_dir / "model.joblib"
    if model_src.exists():
        shutil.copy2(model_src, package_dir / "model.joblib")
        print("  ✓ Model artifact")
    
    # Copy provenance
    provenance_src = run_dir / "provenance.json"
    if provenance_src.exists():
        shutil.copy2(provenance_src, package_dir / "provenance.json")
        print("  ✓ Provenance manifest")
    
    # Copy metrics
    metrics_src = run_dir / "metrics.json"
    if metrics_src.exists():
        shutil.copy2(metrics_src, package_dir / "metrics.json")
        print("  ✓ Metrics")
    
    # Copy config
    config_src = run_dir / "config_resolved.json"
    if config_src.exists():
        shutil.copy2(config_src, package_dir / "config_resolved.json")
        print("  ✓ Configuration")
    
    # Copy dataset manifest reference
    dataset_manifest_src = run_dir / "dataset_manifest.json"
    if dataset_manifest_src.exists():
        shutil.copy2(dataset_manifest_src, package_dir / "dataset_manifest.json")
        print("  ✓ Dataset manifest")
    
    # Copy report
    report_src = run_dir / "report.md"
    if report_src.exists():
        shutil.copy2(report_src, package_dir / "report.md")
        print("  ✓ Evaluation report")
    
    # Create package manifest
    create_package_manifest(package_dir, run_id)
    
    print(f"✓ Model package created: {package_dir}")
    return package_dir


def create_package_manifest(package_dir: Path, run_id: str) -> None:
    """
    Create a manifest file for the packaged model.
    
    Args:
        package_dir: Package directory
        run_id: Run identifier
    """
    manifest = {
        "package_id": run_id,
        "package_type": "ml_model",
        "package_version": "1.0",
        "contents": []
    }
    
    # List all files in package
    for file_path in package_dir.iterdir():
        if file_path.is_file() and file_path.name != "package_manifest.json":
            manifest["contents"].append({
                "file": file_path.name,
                "size_bytes": file_path.stat().st_size
            })
    
    # Save manifest
    manifest_path = package_dir / "package_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    
    print("  ✓ Package manifest")


def load_model_from_package(package_dir: Path) -> Any:
    """
    Load model from a packaged directory.
    
    Args:
        package_dir: Package directory
    
    Returns:
        Loaded model
    """
    model_path = package_dir / "model.joblib"
    if not model_path.exists():
        raise FileNotFoundError(f"Model not found in package: {package_dir}")
    
    return joblib.load(model_path)


def get_package_info(package_dir: Path) -> Dict[str, Any]:
    """
    Get information about a packaged model.
    
    Args:
        package_dir: Package directory
    
    Returns:
        Dictionary with package information
    """
    info = {
        "package_dir": str(package_dir),
        "exists": package_dir.exists()
    }
    
    if not package_dir.exists():
        return info
    
    # Load provenance
    provenance_path = package_dir / "provenance.json"
    if provenance_path.exists():
        with open(provenance_path) as f:
            info["provenance"] = json.load(f)
    
    # Load metrics
    metrics_path = package_dir / "metrics.json"
    if metrics_path.exists():
        with open(metrics_path) as f:
            info["metrics"] = json.load(f)
    
    # Load package manifest
    manifest_path = package_dir / "package_manifest.json"
    if manifest_path.exists():
        with open(manifest_path) as f:
            info["manifest"] = json.load(f)
    
    return info
