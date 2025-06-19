from factor_pipeline.base.BaseScorer import BaseScorer
import pandas as pd
import joblib

class ValueScorer(BaseScorer):
    """
    Applies a trained ML model to compute value scores from standardized features.
    """

    def __init__(self, model_path: str, features: list[str]):
        self.model_path = model_path
        self.features = features
        self.model = joblib.load(model_path)

    def score(self, df: pd.DataFrame) -> pd.Series:
        if not all(f in df.columns for f in self.features):
            missing = set(self.features) - set(df.columns)
            raise ValueError(f"Missing required features: {missing}")

        scores = self.model.predict(df[self.features])
        return pd.Series(scores, index=df.index, name="value_score")
