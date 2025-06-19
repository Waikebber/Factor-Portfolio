# value_factor_trainer.py
from factor_pipeline.base.BaseTrainer import BaseTrainer
from factor_pipeline.pipeline.FeatureTransformer import FeatureTransformer
import pandas as pd

class ValueFactorTrainer(BaseTrainer):
    """
    Trains a regression model to predict next-period returns based on value signals.
    """

    def __init__(self, model_path: str, model_type: str, model_params: dict):
        super().__init__(model_path, model_type, model_params)
        self.features = [
            "price_to_earnings_ratio",
            "price_to_book_ratio",
            "price_to_sales_ratio",
            "price_to_free_cash_flow_ratio",
            "free_cash_flow_yield",
            "earnings_yield",
            "graham_number",
            "return_on_equity",
            "return_on_assets"
        ]

    def preprocess_data(self, df: pd.DataFrame, training_cols: list[str], target_col: str = "next_return"):
        df = FeatureTransformer.winsorize(df, self.features)
        df = FeatureTransformer.zscore_columns(df, self.features)
        df = FeatureTransformer.compute_forward_return(df, price_col="close", horizon=1)
        df = df.dropna(subset=[target_col])
        X = df[training_cols]
        y = df[target_col]
        mask = y.notna() & X.notna().all(axis=1)
        return X.loc[mask], y.loc[mask]

    def fit(self, X: pd.DataFrame, y: pd.Series) -> dict:
        try:
            self.model.fit(X, y)
            self.save()
            return {
                "model": self.model,
                "train_size": len(y),
                "model_path": self.model_path,
                "weights_map": self._get_weights_map(X.columns.tolist(),)
            }
        except Exception as e:
            raise RuntimeError(f"Training failed: {e}")
        
    def _get_weights_map(self, features: list[str]):
        """Get the feature and its weight"""
        weights = self.get_model_weights()
        return {feature: weight for feature, weight in zip(features, weights)}

