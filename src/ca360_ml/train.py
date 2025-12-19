"""
Training utilities for baseline ML models.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

from .reproducibility import set_seed


def create_model(model_type: str, hyperparameters: Dict[str, Any]) -> Any:
    """
    Create model based on configuration.
    
    Args:
        model_type: Type of model to create
        hyperparameters: Model hyperparameters
    
    Returns:
        Initialized model
    """
    if model_type == "sklearn_random_forest":
        return RandomForestClassifier(**hyperparameters)
    elif model_type == "sklearn_logistic":
        return LogisticRegression(**hyperparameters)
    elif model_type == "sklearn_svm":
        return SVC(**hyperparameters)
    else:
        raise ValueError(f"Unknown model type: {model_type}")


def train_model(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_val: Optional[pd.DataFrame],
    y_val: Optional[pd.Series],
    config: Dict[str, Any],
    run_dir: Path
) -> Any:
    """
    Train model according to configuration.
    
    Args:
        X_train: Training features
        y_train: Training labels
        X_val: Validation features (optional)
        y_val: Validation labels (optional)
        config: Training configuration
        run_dir: Directory to save training artifacts
    
    Returns:
        Trained model
    """
    training_config = config.get("training", {})
    
    # Set seed for reproducibility
    seed = training_config.get("seed", 42)
    set_seed(seed)
    
    # Create model
    model_type = training_config.get("model_type", "sklearn_random_forest")
    hyperparameters = training_config.get("hyperparameters", {})
    
    print(f"Creating model: {model_type}")
    model = create_model(model_type, hyperparameters)
    
    # Train model
    print(f"Training on {X_train.shape[0]} samples...")
    start_time = datetime.now()
    
    model.fit(X_train, y_train)
    
    train_time = (datetime.now() - start_time).total_seconds()
    print(f"Training completed in {train_time:.2f}s")
    
    # Save model
    model_path = run_dir / "model.joblib"
    joblib.dump(model, model_path)
    print(f"Model saved to: {model_path}")
    
    # Save training metadata
    metadata = {
        "model_type": model_type,
        "hyperparameters": hyperparameters,
        "training_samples": int(X_train.shape[0]),
        "training_time_seconds": train_time,
        "features": list(X_train.columns),
        "n_features": int(X_train.shape[1]),
    }
    
    metadata_path = run_dir / "training_metadata.json"
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=2)
    
    return model


def save_config(config: Dict[str, Any], run_dir: Path) -> None:
    """Save resolved configuration to run directory."""
    config_path = run_dir / "config_resolved.yaml"
    
    # Save as JSON for simplicity (YAML would require PyYAML)
    import json
    config_json_path = run_dir / "config_resolved.json"
    with open(config_json_path, "w") as f:
        json.dump(config, f, indent=2)
    
    print(f"Configuration saved to: {config_json_path}")
