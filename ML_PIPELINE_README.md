# CA360 ML Pipeline - Baseline Training Pipeline

This directory contains the baseline training pipeline implementation for AMPEL360 CA360º, providing **reproducible, versioned, and auditable** machine learning model training.

## Overview

The CA360 ML Pipeline implements a **certifiable, deterministic training pipeline** with:

- ✅ **Reproducible runs**: Same code + config + dataset → same metrics
- ✅ **Versioned datasets**: Immutable dataset snapshots with manifests
- ✅ **Automated evaluation**: Standardized metrics + threshold gates
- ✅ **Audit trail**: Complete provenance manifests for every run

## Quick Start

### Installation

```bash
# Install the package (from repository root)
pip install -e .
```

### Basic Usage

```bash
# Validate a dataset manifest
ca360-ml dataset validate --manifest data/manifests/ds_spacet_q10_ata21_v1.0.0.json

# Train a baseline model
ca360-ml train \
  --config configs/ml/baseline.yaml \
  --dataset-manifest data/manifests/ds_spacet_q10_ata21_v1.0.0.json

# Train with CI sample data
ca360-ml train \
  --config configs/ml/baseline.yaml \
  --dataset-manifest data/manifests/ds_spacet_q10_ata21_v1.0.0.json \
  --use-sample

# Evaluate the latest run
ca360-ml eval --last-run --config configs/ml/baseline.yaml

# Check evaluation gates
ca360-ml gate check --last-run --config configs/ml/baseline.yaml

# Package model for deployment
ca360-ml package --last-run
```

## Directory Structure

```
.
├── configs/ml/              # Configuration files
│   ├── baseline.yaml        # Baseline pipeline config
│   ├── dataset.yaml         # Dataset loading config
│   ├── train.yaml           # Training config
│   └── eval.yaml            # Evaluation config
├── data/
│   ├── schemas/             # JSON schemas
│   │   ├── dataset.schema.json
│   │   └── provenance.schema.json
│   ├── manifests/           # Dataset manifests (versioned)
│   │   └── ds_spacet_q10_ata21_v1.0.0.json
│   └── samples/             # CI-safe sample datasets
│       └── ci_sample.csv
├── src/ca360_ml/            # Python package
│   ├── cli.py               # CLI interface
│   ├── data.py              # Data loading/preprocessing
│   ├── train.py             # Training logic
│   ├── eval.py              # Evaluation logic
│   ├── reproducibility.py  # Reproducibility utilities
│   └── package.py           # Model packaging
├── runs/                    # Training runs (gitignored)
├── models/registry/         # Packaged models (gitignored)
└── reports/latest/          # Evaluation reports (gitignored)
```

## Dataset Versioning

Each dataset is versioned with:
- **Semantic version**: e.g., `1.0.0`
- **SHA256 manifest hash**: ensuring immutability
- **Dataset ID**: `<name>:<version>+<hash>`

Example manifest structure:
```json
{
  "dataset_name": "spacet_q10_ata21",
  "dataset_version": "1.0.0",
  "files": [...],
  "splits": {...},
  "provenance": {
    "source": "...",
    "extract_date": "2025-01-01",
    "license": "Internal"
  }
}
```

## Reproducibility Guarantees

Every run produces a provenance manifest containing:
- `git_sha`: Code version
- `dataset_manifest_sha256`: Dataset version
- `config_sha256`: Configuration hash
- `seed`: Random seed
- `env_lock_sha256`: Dependencies hash
- `timestamp_utc`: Run timestamp
- `hardware`: Hardware configuration
- `metrics`: Training/evaluation results

## Evaluation Gates

The pipeline enforces quality gates:

1. **Threshold gates**: Minimum metric requirements
   - Example: `f1 >= 0.90`, `accuracy >= 0.85`

2. **Regression detection**: Compare against baseline
   - Tolerance: 2% degradation allowed by default

3. **Gate enforcement**: PR-blocking in CI

## CI/CD Integration

The pipeline integrates with GitHub Actions:

### Workflow: `train_eval.yml`

Triggered on:
- Pull requests affecting ML code
- Manual workflow dispatch

Steps:
1. Validate dataset manifest
2. Train on CI sample data
3. Evaluate model
4. Check evaluation gates (PR-blocking)
5. Upload run artifacts

### Portal Gates Integration

Gate D validates ML pipeline infrastructure:
- Directory structure
- Core Python files
- Schema definitions
- Configuration files
- Dataset manifests
- Sample data

## Configuration Files

### `baseline.yaml`
Combines all configurations for a complete training pipeline.

### `dataset.yaml`
Dataset loading and preprocessing configuration.

### `train.yaml`
Model architecture and training hyperparameters.

### `eval.yaml`
Evaluation metrics and threshold gates.

## Run Artifacts

Each run produces:
```
runs/<run_id>/
├── provenance.json          # Complete provenance
├── config_resolved.json     # Resolved configuration
├── dataset_manifest.json    # Dataset reference
├── model.joblib             # Trained model
├── metrics.json             # Evaluation metrics
├── training_metadata.json   # Training info
├── confusion_matrix.csv     # Confusion matrix (optional)
└── report.md                # Human-readable report
```

## Model Registry

Packaged models are stored in `models/registry/`:
```
models/registry/<run_id>/
├── model.joblib
├── provenance.json
├── metrics.json
├── config_resolved.json
├── dataset_manifest.json
├── report.md
└── package_manifest.json
```

## Development

### Adding New Models

1. Update `train.py` with new model type
2. Add hyperparameters to `train.yaml`
3. Update evaluation metrics if needed

### Adding New Metrics

1. Update `eval.py` with metric computation
2. Add to `eval.yaml` metrics list
3. Add threshold if needed

### Testing

```bash
# Run with sample data
ca360-ml train --config configs/ml/baseline.yaml \
  --dataset-manifest data/manifests/ds_spacet_q10_ata21_v1.0.0.json \
  --use-sample

# Check gates
ca360-ml gate check --last-run --config configs/ml/baseline.yaml
```

## Integration with CA360º Governance

The ML pipeline aligns with CA360º governance:

- **VSN/MSN binding**: Link models to vision/mission statements
- **SSOT page**: Single source of truth for baseline models
- **AoR constraints**: Model governance under STK_AI
- **LC06 integration**: Acceptability decision references
- **Evidence packs**: Run bundles as certification evidence

## Future Enhancements

Planned additions:
- DVC integration for large datasets
- MLflow tracking
- ONNX model export
- Cross-validation support
- Hyperparameter tuning
- Model comparison tools

## Contact

For questions about the ML pipeline, contact the AMPEL360 ML team.
