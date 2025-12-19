# Enhanced ML Pipeline Features

This document describes the advanced features added to the CA360 ML Pipeline.

## Overview

The enhanced pipeline now includes:
1. **DVC Integration** - Large dataset versioning with remote storage
2. **MLflow Tracking** - Centralized experiment tracking
3. **ONNX Export** - Cross-platform model deployment
4. **Hyperparameter Tuning** - Automated optimization with Optuna
5. **Cross-Validation** - Advanced evaluation strategies
6. **Model Comparison** - Interactive dashboards for comparing models

## Installation

Install enhanced features with optional dependencies:

```bash
# Install all enhanced features
pip install -e ".[all]"

# Or install specific features
pip install -e ".[dvc]"      # DVC integration
pip install -e ".[mlflow]"   # MLflow tracking
pip install -e ".[onnx]"     # ONNX export
pip install -e ".[tuning]"   # Hyperparameter tuning
```

## 1. DVC Integration

### Setup

Initialize DVC in your repository:

```bash
# Install DVC with S3 support
pip install -e ".[dvc]"

# Initialize DVC (done once)
dvc init

# Configure remote storage
dvc remote add -d myremote s3://mybucket/path
```

### Usage in Python

```python
from ca360_ml.dvc_integration import DVCManager

# Create DVC manager
dvc = DVCManager()

# Add dataset to DVC tracking
dvc.add_dataset("data/large_dataset.csv")

# Push to remote
dvc.push()

# Pull from remote (on another machine)
dvc.pull()
```

### Benefits

- **Version control** for large datasets without storing them in Git
- **Remote storage** (S3, GCS, Azure) for team collaboration
- **Reproducibility** - Pin exact dataset versions to model runs

## 2. MLflow Tracking

### Setup

```bash
# Install MLflow
pip install -e ".[mlflow]"

# Start local MLflow server (optional)
mlflow ui
```

### Track Training Runs

```bash
# Track an existing run in MLflow
ca360-ml mlflow track --run-id run_20251219_180446 \
  --tracking-uri http://localhost:5000
```

### Python API

```python
from ca360_ml.mlflow_integration import track_training_run

# Track complete training run
mlflow_run_id = track_training_run(
    run_name="baseline_v1",
    config=config,
    metrics=metrics,
    model=model,
    provenance=provenance,
    tracking_uri="http://localhost:5000",
    register_model=True,
    model_name="ca360_baseline"
)
```

### Compare Runs

```python
from ca360_ml.mlflow_integration import compare_runs, get_best_run

# Compare multiple runs
comparison = compare_runs(
    ["run_id_1", "run_id_2", "run_id_3"],
    tracking_uri="http://localhost:5000"
)

# Get best run
best = get_best_run(
    experiment_name="ca360_ml",
    metric="f1",
    tracking_uri="http://localhost:5000"
)
```

## 3. ONNX Model Export

### Export via CLI

```bash
# Export model to ONNX format
ca360-ml export-onnx \
  --model-path runs/run_20251219_180446/model.joblib \
  --n-features 3 \
  --output model.onnx
```

### Python API

```python
from ca360_ml.onnx_export import (
    export_sklearn_to_onnx,
    validate_onnx_model,
    infer_onnx_model
)

# Export model
onnx_path = export_sklearn_to_onnx(
    model=trained_model,
    n_features=3,
    output_path=Path("model.onnx")
)

# Validate ONNX model
is_valid = validate_onnx_model(onnx_path)

# Run inference
predictions = infer_onnx_model(
    onnx_path,
    input_data=test_data
)
```

### Benefits

- **Cross-platform deployment** - Run on any ONNX runtime
- **Performance optimization** - Hardware-accelerated inference
- **Language agnostic** - Use from C++, C#, Java, JavaScript
- **Mobile/Edge deployment** - Deploy to iOS, Android, embedded devices

## 4. Hyperparameter Tuning

### Automated Tuning with Optuna

```bash
# Tune hyperparameters
ca360-ml tune \
  --config configs/ml/baseline.yaml \
  --dataset-manifest data/manifests/ds_spacet_q10_ata21_v1.0.0.json \
  --n-trials 100 \
  --use-sample
```

### Python API

```python
from ca360_ml.hyperparameter_tuning import (
    OptunaHyperparameterTuner,
    tune_random_forest
)

# Quick tuning for Random Forest
results = tune_random_forest(
    X_train, y_train,
    n_trials=50,
    cv_folds=5
)

print(f"Best parameters: {results['best_params']}")
print(f"Best score: {results['best_score']}")

# Custom tuning
def model_factory(**params):
    return RandomForestClassifier(**params)

param_space = {
    "n_estimators": {"type": "int", "low": 10, "high": 300},
    "max_depth": {"type": "int", "low": 3, "high": 30},
}

tuner = OptunaHyperparameterTuner(
    model_factory=model_factory,
    param_space=param_space,
    n_trials=100
)

results = tuner.tune(X_train, y_train)
```

### Features

- **Efficient search** - Uses Bayesian optimization
- **Parallel trials** - Runs multiple trials concurrently
- **Pruning** - Stops unpromising trials early
- **Visualization** - Built-in optimization history plots

## 5. Cross-Validation

### CLI

```bash
# Perform k-fold cross-validation
ca360-ml cross-validate \
  --config configs/ml/baseline.yaml \
  --dataset-manifest data/manifests/ds_spacet_q10_ata21_v1.0.0.json \
  --n-folds 10 \
  --use-sample
```

### Python API

```python
from ca360_ml.cross_validation import (
    perform_k_fold_cv,
    nested_cross_validation,
    perform_time_series_cv
)

# Standard k-fold CV
cv_results = perform_k_fold_cv(
    model, X, y,
    n_folds=5,
    stratified=True
)

# Nested CV for unbiased evaluation
nested_results = nested_cross_validation(
    model, param_grid, X, y,
    outer_cv=5,
    inner_cv=3
)

# Time series CV
ts_results = perform_time_series_cv(
    model, X, y,
    n_splits=5
)
```

### Strategies Available

- **K-Fold CV** - Standard cross-validation
- **Stratified K-Fold** - Preserves class distribution
- **Time Series Split** - For temporal data
- **Nested CV** - Unbiased hyperparameter tuning
- **Leave-One-Out** - For small datasets

## 6. Model Comparison Dashboard

### Compare Multiple Models

```bash
# Compare multiple runs
ca360-ml compare \
  --run-ids run_20251219_180446 \
  --run-ids run_20251219_181234 \
  --run-ids run_20251219_182345 \
  --output-dir reports/comparison
```

### Python API

```python
from ca360_ml.model_comparison import (
    generate_comparison_report,
    create_metrics_comparison_chart,
    rank_models
)

# Generate full comparison report
model_results = {
    "Model A": {"metrics": {...}, "training_time": 10.5},
    "Model B": {"metrics": {...}, "training_time": 15.2},
}

generate_comparison_report(
    model_results,
    output_dir=Path("reports/comparison")
)

# Rank models
rankings = rank_models(
    model_results,
    primary_metric="f1",
    secondary_metric="accuracy"
)
```

### Generated Outputs

- **metrics_comparison.html** - Interactive bar charts
- **time_comparison.html** - Training time visualization
- **comparison_summary.csv** - Tabular results
- **comparison_report.md** - Markdown summary

## Workflow Examples

### Complete Workflow with All Features

```bash
# 1. Train baseline model
ca360-ml train \
  --config configs/ml/baseline.yaml \
  --dataset-manifest data/manifests/ds_spacet_q10_ata21_v1.0.0.json

# 2. Perform cross-validation
ca360-ml cross-validate \
  --config configs/ml/baseline.yaml \
  --dataset-manifest data/manifests/ds_spacet_q10_ata21_v1.0.0.json \
  --n-folds 10

# 3. Tune hyperparameters
ca360-ml tune \
  --config configs/ml/baseline.yaml \
  --dataset-manifest data/manifests/ds_spacet_q10_ata21_v1.0.0.json \
  --n-trials 100

# 4. Train with best parameters
# (Update config with tuned params, then retrain)
ca360-ml train --config configs/ml/baseline_tuned.yaml \
  --dataset-manifest data/manifests/ds_spacet_q10_ata21_v1.0.0.json

# 5. Export to ONNX
ca360-ml export-onnx \
  --model-path runs/<run_id>/model.joblib \
  --n-features 3 \
  --output model.onnx

# 6. Track in MLflow
ca360-ml mlflow track --run-id <run_id> \
  --tracking-uri http://localhost:5000

# 7. Compare models
ca360-ml compare \
  --run-ids <run_id_1> \
  --run-ids <run_id_2> \
  --output-dir reports/comparison
```

## Best Practices

### DVC
- Initialize DVC early in the project
- Use meaningful commit messages for data changes
- Set up remote storage for team collaboration
- Document dataset provenance in manifests

### MLflow
- Use consistent experiment naming
- Tag runs with meaningful metadata
- Register best models for easy retrieval
- Set up a shared tracking server for teams

### ONNX
- Validate ONNX models after export
- Test inference with sample data
- Document input/output specifications
- Version ONNX models alongside Python models

### Hyperparameter Tuning
- Start with a small number of trials (10-20)
- Use cross-validation in the objective function
- Save tuning results for reproducibility
- Document the search space used

### Cross-Validation
- Use stratified CV for imbalanced datasets
- Choose appropriate number of folds (5-10)
- Use nested CV when tuning hyperparameters
- Report both mean and std of metrics

### Model Comparison
- Compare models on the same dataset splits
- Include training time in comparisons
- Generate visualizations for stakeholders
- Document model selection rationale

## Configuration

Add enhanced feature settings to your `baseline.yaml`:

```yaml
# Enhanced features configuration
enhanced:
  dvc:
    enabled: true
    remote: "myremote"
  
  mlflow:
    enabled: true
    tracking_uri: "http://localhost:5000"
    experiment_name: "ca360_ml"
  
  onnx:
    enabled: true
    export_on_train: false
  
  tuning:
    enabled: false
    n_trials: 50
    metric: "f1"
  
  cross_validation:
    enabled: false
    n_folds: 5
    stratified: true
```

## Troubleshooting

### DVC Issues
- **Problem**: `dvc push` fails
- **Solution**: Check remote credentials and connectivity

### MLflow Issues
- **Problem**: Cannot connect to tracking server
- **Solution**: Verify tracking URI and ensure server is running

### ONNX Issues
- **Problem**: Export fails for custom models
- **Solution**: Ensure model is supported by skl2onnx

### Tuning Issues
- **Problem**: Tuning is very slow
- **Solution**: Reduce n_trials or use faster CV strategy

## Next Steps

- Set up DVC remote storage for your team
- Deploy MLflow tracking server
- Integrate ONNX models into production pipelines
- Automate hyperparameter tuning in CI/CD
- Create dashboards for continuous model monitoring
