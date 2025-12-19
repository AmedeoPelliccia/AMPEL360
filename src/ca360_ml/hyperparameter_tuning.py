"""
Hyperparameter tuning with Optuna and scikit-optimize.

Provides automated hyperparameter optimization for ML models.
"""

import json
from pathlib import Path
from typing import Any, Callable, Dict, Optional, Tuple

import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score

try:
    import optuna
    OPTUNA_AVAILABLE = True
except ImportError:
    OPTUNA_AVAILABLE = False

try:
    from skopt import BayesSearchCV
    from skopt.space import Real, Integer, Categorical
    SKOPT_AVAILABLE = True
except ImportError:
    SKOPT_AVAILABLE = False


class OptunaHyperparameterTuner:
    """Hyperparameter tuning using Optuna."""
    
    def __init__(
        self,
        model_factory: Callable,
        param_space: Dict[str, Any],
        metric: str = "f1_weighted",
        n_trials: int = 100,
        cv_folds: int = 5
    ):
        """
        Initialize Optuna tuner.
        
        Args:
            model_factory: Function that creates a model given hyperparameters
            param_space: Dictionary defining hyperparameter search space
            metric: Metric to optimize
            n_trials: Number of trials to run
            cv_folds: Number of cross-validation folds
        """
        if not OPTUNA_AVAILABLE:
            raise ImportError("Optuna not installed. Install with: pip install optuna")
        
        self.model_factory = model_factory
        self.param_space = param_space
        self.metric = metric
        self.n_trials = n_trials
        self.cv_folds = cv_folds
        self.study = None
        self.best_params = None
        self.best_score = None
    
    def objective(self, trial: Any, X: pd.DataFrame, y: pd.Series) -> float:
        """
        Objective function for optimization.
        
        Args:
            trial: Optuna trial object
            X: Training features
            y: Training labels
        
        Returns:
            Score to optimize
        """
        # Suggest hyperparameters
        params = {}
        for param_name, param_config in self.param_space.items():
            if param_config["type"] == "int":
                params[param_name] = trial.suggest_int(
                    param_name,
                    param_config["low"],
                    param_config["high"]
                )
            elif param_config["type"] == "float":
                params[param_name] = trial.suggest_float(
                    param_name,
                    param_config["low"],
                    param_config["high"],
                    log=param_config.get("log", False)
                )
            elif param_config["type"] == "categorical":
                params[param_name] = trial.suggest_categorical(
                    param_name,
                    param_config["choices"]
                )
        
        # Create model with suggested parameters
        model = self.model_factory(**params)
        
        # Evaluate with cross-validation
        scores = cross_val_score(
            model, X, y,
            cv=self.cv_folds,
            scoring=self.metric
        )
        
        return scores.mean()
    
    def tune(
        self,
        X: pd.DataFrame,
        y: pd.Series,
        study_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Run hyperparameter tuning.
        
        Args:
            X: Training features
            y: Training labels
            study_name: Name for the study
        
        Returns:
            Dictionary with best parameters and score
        """
        print(f"Starting hyperparameter tuning with {self.n_trials} trials...")
        
        # Create study
        self.study = optuna.create_study(
            study_name=study_name,
            direction="maximize"
        )
        
        # Optimize
        self.study.optimize(
            lambda trial: self.objective(trial, X, y),
            n_trials=self.n_trials,
            show_progress_bar=True
        )
        
        # Store results
        self.best_params = self.study.best_params
        self.best_score = self.study.best_value
        
        print(f"✓ Best {self.metric}: {self.best_score:.4f}")
        print(f"✓ Best parameters: {self.best_params}")
        
        return {
            "best_params": self.best_params,
            "best_score": self.best_score,
            "n_trials": self.n_trials,
            "study_name": study_name
        }
    
    def get_optimization_history(self) -> pd.DataFrame:
        """
        Get optimization history as DataFrame.
        
        Returns:
            DataFrame with trial results
        """
        if self.study is None:
            return pd.DataFrame()
        
        trials = self.study.trials
        history = []
        
        for trial in trials:
            row = {
                "trial_number": trial.number,
                "value": trial.value,
                "state": trial.state.name,
                **trial.params
            }
            history.append(row)
        
        return pd.DataFrame(history)
    
    def save_study(self, output_path: Path) -> None:
        """
        Save study results to file.
        
        Args:
            output_path: Path to save results
        """
        if self.study is None:
            print("⚠ No study to save")
            return
        
        results = {
            "best_params": self.best_params,
            "best_score": self.best_score,
            "n_trials": len(self.study.trials),
            "optimization_history": self.get_optimization_history().to_dict("records")
        }
        
        with open(output_path, "w") as f:
            json.dump(results, f, indent=2)
        
        print(f"✓ Saved study results to {output_path}")


def tune_random_forest(
    X: pd.DataFrame,
    y: pd.Series,
    n_trials: int = 50,
    cv_folds: int = 5
) -> Dict[str, Any]:
    """
    Tune Random Forest hyperparameters.
    
    Args:
        X: Training features
        y: Training labels
        n_trials: Number of trials
        cv_folds: Number of CV folds
    
    Returns:
        Best parameters and score
    """
    from sklearn.ensemble import RandomForestClassifier
    
    def model_factory(**params):
        return RandomForestClassifier(**params, random_state=42)
    
    param_space = {
        "n_estimators": {"type": "int", "low": 10, "high": 300},
        "max_depth": {"type": "int", "low": 3, "high": 30},
        "min_samples_split": {"type": "int", "low": 2, "high": 20},
        "min_samples_leaf": {"type": "int", "low": 1, "high": 10},
        "max_features": {"type": "categorical", "choices": ["sqrt", "log2", None]},
    }
    
    tuner = OptunaHyperparameterTuner(
        model_factory=model_factory,
        param_space=param_space,
        n_trials=n_trials,
        cv_folds=cv_folds
    )
    
    return tuner.tune(X, y, study_name="random_forest_tuning")


def tune_with_bayesian_search(
    model: Any,
    param_space: Dict[str, Any],
    X: pd.DataFrame,
    y: pd.Series,
    n_iter: int = 50,
    cv_folds: int = 5,
    scoring: str = "f1_weighted"
) -> Tuple[Any, Dict[str, Any]]:
    """
    Tune hyperparameters using Bayesian optimization.
    
    Args:
        model: Model to tune
        param_space: Search space for parameters
        X: Training features
        y: Training labels
        n_iter: Number of iterations
        cv_folds: Number of CV folds
        scoring: Scoring metric
    
    Returns:
        Tuple of (best_estimator, results_dict)
    """
    if not SKOPT_AVAILABLE:
        raise ImportError("scikit-optimize not installed. Install with: pip install scikit-optimize")
    
    print(f"Starting Bayesian hyperparameter search with {n_iter} iterations...")
    
    # Convert param space to skopt format
    skopt_space = {}
    for param_name, param_config in param_space.items():
        if param_config["type"] == "int":
            skopt_space[param_name] = Integer(
                param_config["low"],
                param_config["high"]
            )
        elif param_config["type"] == "float":
            skopt_space[param_name] = Real(
                param_config["low"],
                param_config["high"],
                prior="log-uniform" if param_config.get("log", False) else "uniform"
            )
        elif param_config["type"] == "categorical":
            skopt_space[param_name] = Categorical(param_config["choices"])
    
    # Run Bayesian search
    search = BayesSearchCV(
        model,
        skopt_space,
        n_iter=n_iter,
        cv=cv_folds,
        scoring=scoring,
        n_jobs=-1,
        random_state=42
    )
    
    search.fit(X, y)
    
    print(f"✓ Best {scoring}: {search.best_score_:.4f}")
    print(f"✓ Best parameters: {search.best_params_}")
    
    results = {
        "best_params": search.best_params_,
        "best_score": search.best_score_,
        "cv_results": search.cv_results_
    }
    
    return search.best_estimator_, results


def grid_search_with_validation(
    model: Any,
    param_grid: Dict[str, list],
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_val: pd.DataFrame,
    y_val: pd.Series,
    scoring: str = "f1_weighted"
) -> Tuple[Any, Dict[str, Any]]:
    """
    Grid search with separate validation set.
    
    Args:
        model: Model to tune
        param_grid: Grid of parameters to search
        X_train: Training features
        y_train: Training labels
        X_val: Validation features
        y_val: Validation labels
        scoring: Scoring metric
    
    Returns:
        Tuple of (best_model, results_dict)
    """
    from sklearn.model_selection import ParameterGrid
    from sklearn.metrics import get_scorer
    
    scorer = get_scorer(scoring)
    
    best_score = -np.inf
    best_params = None
    best_model = None
    results = []
    
    print(f"Starting grid search with {len(ParameterGrid(param_grid))} combinations...")
    
    for params in ParameterGrid(param_grid):
        # Train model with params
        model.set_params(**params)
        model.fit(X_train, y_train)
        
        # Evaluate on validation set
        score = scorer(model, X_val, y_val)
        
        results.append({
            "params": params,
            "score": score
        })
        
        if score > best_score:
            best_score = score
            best_params = params
            best_model = model
    
    print(f"✓ Best {scoring}: {best_score:.4f}")
    print(f"✓ Best parameters: {best_params}")
    
    return best_model, {
        "best_params": best_params,
        "best_score": best_score,
        "all_results": results
    }
