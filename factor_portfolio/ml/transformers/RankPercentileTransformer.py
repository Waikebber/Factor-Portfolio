import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class RankPercentileTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, columns: list):
        self.columns = columns

    def fit(self, X: pd.DataFrame, y=None):
        # No fitting necessary for percentile ranking
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X_copy = X.copy()
        for col in self.columns:
            X_copy[col + "_pct"] = X_copy[col].rank(pct=True)
        return X_copy
