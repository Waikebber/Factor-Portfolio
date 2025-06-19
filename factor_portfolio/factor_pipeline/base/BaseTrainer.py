# base_trainer.py
from abc import ABC, abstractmethod
import os
from datetime import datetime
from typing import Optional
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
import pandas as pd

class BaseTrainer(ABC):
    """
    Abstract trainer class for regression or ML-based factor training.
    """

    def __init__(self, model_path: Optional[str], model_type: str, model_params: dict):
        self.model_path = model_path
        self.model_type = model_type
        self.model_params = model_params
        self.model = self._initialize_model()

    def _initialize_model(self):
        if self.model_type == "linear":
            return LinearRegression(**self.model_params)
        elif self.model_type == "random_forest":
            return RandomForestRegressor(**self.model_params)
        elif self.model_type == "xgboost":
            return XGBRegressor(**self.model_params)
        elif self.model_type == "gbr":
            return GradientBoostingRegressor(**self.model_params)
        else:
            raise ValueError(f"Unsupported model_type: {self.model_type}")

    def get_default_model_path(self):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return f"models/{self.model_type.replace('_', '-')}-model_{timestamp}.pkl"

    def save(self):
        if self.model_path is None:
            os.makedirs("models", exist_ok=True)
            self.model_path = self.get_default_model_path()
        joblib.dump(self.model, self.model_path)

    def load(self):
        if self.model_path is None:
            raise ValueError("No model path provided.")
        self.model = joblib.load(self.model_path)

    def get_model_weights(self):
        match self.model_type:
            case "linear":
                return getattr(self.model, "coef_", None)
            case "random_forest" | "xgboost" | "gbr":
                return self.model.feature_importances_

    def get_model_details(self):
        return {
            "model_type": self.model_type,
            "model_params": self.model_params,
            "model_path": self.model_path,
            "model_weights": self.get_model_weights()
        }

    @abstractmethod
    def fit(self, X: pd.DataFrame, y: pd.Series) -> dict:
        pass

    @abstractmethod
    def preprocess_data(self, df: pd.DataFrame, training_cols: list[str], target_col: str = "next_return"):
        pass
