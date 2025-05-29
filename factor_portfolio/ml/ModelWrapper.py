import joblib, os, json
import pandas as pd
from datetime import datetime, UTC
from .BaseModel import BaseModel
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

MODEL_CLASSES = {
    "lasso": Lasso,
    "random_forest": RandomForestRegressor,
    "xgboost": XGBRegressor
}

class ModelWrapper(BaseModel):
    def __init__(self, model_type: str, features: list, hyperparams: dict, model_path: str):
        if model_type not in MODEL_CLASSES:
            raise ValueError(f"Unsupported model type: '{model_type}'. Must be one of {list(MODEL_CLASSES.keys())}")
        
        self.model_type = model_type
        self.features = features
        self.hyperparams = hyperparams
        self.model_path = model_path
        self.model = MODEL_CLASSES[model_type](**hyperparams)

    def fit(self, X: pd.DataFrame, y: pd.Series):
        self.model.fit(X[self.features].fillna(0), y)

    def predict(self, X: pd.DataFrame) -> pd.Series:
        return pd.Series(self.model.predict(X[self.features].fillna(0)), index=X.index)

    def save(self, path: str = None):
        path = path or self.model_path
        joblib.dump(self.model, path)
        self.save_metadata(path)

    def load(self, path: str = None):
        path = path or self.model_path
        self.model = joblib.load(path)

        meta = self.load_metadata(path)
        if meta:
            self.model_type = meta.get("model_type", self.model_type)
            self.features = meta.get("features", self.features)
            self.hyperparams = meta.get("hyperparameters", self.hyperparams)

    def save_metadata(self, path: str):
        meta = {
            "model_type": self.model_type,
            "features": self.features,
            "hyperparameters": self.hyperparams,
            "saved_at": datetime.now(UTC).isoformat(),
            "version": 1
        }
        meta_path = path.replace(".pkl", ".meta.json")
        with open(meta_path, "w") as f:
            json.dump(meta, f, indent=2)

    def load_metadata(self, path: str = None) -> dict:
        path = path or self.model_path
        meta_path = path.replace(".pkl", ".meta.json")
        if not os.path.exists(meta_path):
            return {}
        with open(meta_path, "r") as f:
            return json.load(f)
    
    def evaluate(self, X: pd.DataFrame, y: pd.Series, metric: str = "r2") -> float:
        X_eval = X[self.features].fillna(0)
        y_pred = self.model.predict(X_eval)

        if metric == "r2":
            return self.model.score(X_eval, y)
        elif metric == "mse":
            return mean_squared_error(y, y_pred)
        else:
            raise ValueError(f"Unsupported metric: {metric}")

