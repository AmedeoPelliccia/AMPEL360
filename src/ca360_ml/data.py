"""
Data handling utilities for dataset loading and validation.
"""

import json
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

import pandas as pd
from sklearn.model_selection import train_test_split


def validate_dataset_manifest(manifest_path: Path) -> bool:
    """
    Validate dataset manifest against schema.
    
    Args:
        manifest_path: Path to dataset manifest JSON file
    
    Returns:
        True if valid, False otherwise
    """
    try:
        with open(manifest_path) as f:
            manifest = json.load(f)
        
        required_fields = [
            "dataset_name",
            "dataset_version",
            "schema_version",
            "files",
            "splits",
            "provenance"
        ]
        
        for field in required_fields:
            if field not in manifest:
                print(f"❌ Missing required field: {field}")
                return False
        
        # Validate provenance
        provenance = manifest["provenance"]
        required_prov_fields = ["source", "extract_date"]
        for field in required_prov_fields:
            if field not in provenance:
                print(f"❌ Missing provenance field: {field}")
                return False
        
        print(f"✓ Dataset manifest valid: {manifest['dataset_name']} v{manifest['dataset_version']}")
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return False
    except Exception as e:
        print(f"❌ Validation error: {e}")
        return False


def load_dataset_from_manifest(
    manifest_path: Path,
    use_sample: bool = False,
    sample_path: Optional[Path] = None
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """
    Load dataset based on manifest specification.
    
    Args:
        manifest_path: Path to dataset manifest
        use_sample: Whether to use sample dataset
        sample_path: Path to sample dataset (if use_sample=True)
    
    Returns:
        Tuple of (dataframe, manifest_dict)
    """
    with open(manifest_path) as f:
        manifest = json.load(f)
    
    if use_sample and sample_path:
        print(f"Loading sample dataset from: {sample_path}")
        df = pd.read_csv(sample_path)
    else:
        # Load from manifest files list
        if not manifest["files"]:
            raise ValueError("No files specified in manifest")
        
        file_info = manifest["files"][0]
        file_path = Path(file_info["path"])
        print(f"Loading dataset from: {file_path}")
        df = pd.read_csv(file_path)
    
    print(f"Dataset shape: {df.shape}")
    return df, manifest


def split_dataset(
    df: pd.DataFrame,
    config: Dict[str, Any],
    target_column: str = "target"
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.Series, pd.Series, pd.Series]:
    """
    Split dataset into train/val/test sets.
    
    Args:
        df: Input dataframe
        config: Configuration with split ratios and seed
        target_column: Name of the target column
    
    Returns:
        Tuple of (X_train, X_val, X_test, y_train, y_val, y_test)
    """
    splits = config.get("splits", {})
    train_ratio = splits.get("train", 0.7)
    val_ratio = splits.get("val", 0.15)
    test_ratio = splits.get("test", 0.15)
    seed = splits.get("split_seed", 42)
    
    # Validate ratios
    total_ratio = train_ratio + val_ratio + test_ratio
    if not (0.99 <= total_ratio <= 1.01):
        raise ValueError(f"Split ratios must sum to 1.0, got {total_ratio}")
    
    # Separate features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # First split: train vs (val + test)
    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y,
        test_size=(val_ratio + test_ratio),
        random_state=seed,
        stratify=y if len(y.unique()) < 10 else None
    )
    
    # Second split: val vs test
    val_test_ratio = val_ratio / (val_ratio + test_ratio)
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp,
        test_size=(1 - val_test_ratio),
        random_state=seed,
        stratify=y_temp if len(y_temp.unique()) < 10 else None
    )
    
    print(f"Train set: {X_train.shape[0]} samples")
    print(f"Val set: {X_val.shape[0]} samples")
    print(f"Test set: {X_test.shape[0]} samples")
    
    return X_train, X_val, X_test, y_train, y_val, y_test


def preprocess_data(
    X_train: pd.DataFrame,
    X_val: pd.DataFrame,
    X_test: pd.DataFrame,
    config: Dict[str, Any]
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Preprocess data according to configuration.
    
    Args:
        X_train: Training features
        X_val: Validation features
        X_test: Test features
        config: Preprocessing configuration
    
    Returns:
        Tuple of preprocessed (X_train, X_val, X_test)
    """
    preprocessing = config.get("preprocessing", {})
    
    # Handle missing values
    if preprocessing.get("handle_missing") == "drop":
        X_train = X_train.dropna()
        X_val = X_val.dropna()
        X_test = X_test.dropna()
    
    # Normalization (fit on train, transform all)
    if preprocessing.get("normalize", False):
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        X_train = pd.DataFrame(
            scaler.fit_transform(X_train),
            columns=X_train.columns,
            index=X_train.index
        )
        X_val = pd.DataFrame(
            scaler.transform(X_val),
            columns=X_val.columns,
            index=X_val.index
        )
        X_test = pd.DataFrame(
            scaler.transform(X_test),
            columns=X_test.columns,
            index=X_test.index
        )
    
    return X_train, X_val, X_test
