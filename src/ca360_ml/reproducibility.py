"""
Reproducibility utilities for deterministic ML training.

Ensures reproducible runs: same code + same config + same dataset => same metrics.
"""

import hashlib
import json
import os
import platform
import random
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

import numpy as np


def set_seed(seed: int) -> None:
    """Set global random seeds for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    
    # Set framework-specific seeds if available
    try:
        import torch
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
            torch.backends.cudnn.deterministic = True
            torch.backends.cudnn.benchmark = False
    except ImportError:
        pass


def get_git_info() -> Dict[str, Any]:
    """Get git repository information."""
    try:
        git_sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], 
            stderr=subprocess.DEVNULL
        ).decode().strip()
        
        # Check for uncommitted changes
        status = subprocess.check_output(
            ["git", "status", "--porcelain"],
            stderr=subprocess.DEVNULL
        ).decode().strip()
        
        dirty_state = len(status) > 0
        
        return {
            "git_sha": git_sha,
            "dirty_state": dirty_state
        }
    except (subprocess.CalledProcessError, FileNotFoundError):
        return {
            "git_sha": "unknown",
            "dirty_state": False
        }


def compute_file_hash(file_path: Path) -> str:
    """Compute SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def compute_dict_hash(data: Dict[str, Any]) -> str:
    """Compute SHA256 hash of a dictionary (via JSON serialization)."""
    json_str = json.dumps(data, sort_keys=True)
    return hashlib.sha256(json_str.encode()).hexdigest()


def get_hardware_info() -> Dict[str, Any]:
    """Get hardware configuration information."""
    hardware = {
        "platform": platform.platform(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
    }
    
    try:
        import psutil
        hardware["memory_gb"] = round(psutil.virtual_memory().total / (1024**3), 2)
        hardware["cpu_count"] = psutil.cpu_count()
    except ImportError:
        pass
    
    try:
        import torch
        if torch.cuda.is_available():
            hardware["gpu"] = torch.cuda.get_device_name(0)
            hardware["cuda_version"] = torch.version.cuda
        else:
            hardware["gpu"] = "none"
    except ImportError:
        hardware["gpu"] = "none"
    
    return hardware


def create_provenance_manifest(
    run_id: str,
    dataset_manifest_path: Path,
    config: Dict[str, Any],
    seed: int,
    env_lock_path: Optional[Path] = None,
    metrics: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Create a complete provenance manifest for a training run.
    
    Args:
        run_id: Unique identifier for this run
        dataset_manifest_path: Path to the dataset manifest
        config: Resolved configuration dictionary
        seed: Random seed used
        env_lock_path: Path to environment lock file (e.g., uv.lock)
        metrics: Training/evaluation metrics
    
    Returns:
        Complete provenance manifest dictionary
    """
    git_info = get_git_info()
    
    provenance = {
        "run_id": run_id,
        "git_sha": git_info["git_sha"],
        "dirty_state": git_info["dirty_state"],
        "dataset_manifest_sha256": compute_file_hash(dataset_manifest_path),
        "config_sha256": compute_dict_hash(config),
        "seed": seed,
        "timestamp_utc": datetime.utcnow().isoformat() + "Z",
        "hardware": get_hardware_info(),
        "python_version": platform.python_version(),
    }
    
    # Add environment lock hash if available
    if env_lock_path and env_lock_path.exists():
        provenance["env_lock_sha256"] = compute_file_hash(env_lock_path)
    else:
        provenance["env_lock_sha256"] = "not_available"
    
    # Add framework versions
    framework_versions = {}
    try:
        import sklearn
        framework_versions["sklearn"] = sklearn.__version__
    except ImportError:
        pass
    
    try:
        import torch
        framework_versions["torch"] = torch.__version__
    except ImportError:
        pass
    
    try:
        import tensorflow as tf
        framework_versions["tensorflow"] = tf.__version__
    except ImportError:
        pass
    
    provenance["framework_versions"] = framework_versions
    
    # Add metrics if provided
    if metrics:
        provenance["metrics"] = metrics
    
    # Add dataset ID
    try:
        with open(dataset_manifest_path) as f:
            manifest = json.load(f)
            dataset_id = f"{manifest['dataset_name']}:{manifest['dataset_version']}+{provenance['dataset_manifest_sha256'][:16]}"
            provenance["dataset_id"] = dataset_id
    except Exception:
        provenance["dataset_id"] = "unknown"
    
    return provenance


def validate_provenance(provenance: Dict[str, Any]) -> bool:
    """
    Validate provenance manifest against schema requirements.
    
    Args:
        provenance: Provenance manifest dictionary
    
    Returns:
        True if valid, False otherwise
    """
    required_fields = [
        "run_id",
        "git_sha",
        "dataset_manifest_sha256",
        "config_sha256",
        "seed",
        "timestamp_utc",
        "env_lock_sha256"
    ]
    
    for field in required_fields:
        if field not in provenance:
            print(f"Missing required field: {field}")
            return False
    
    return True
