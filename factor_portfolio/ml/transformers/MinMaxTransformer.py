import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MinMaxScaler

class MinMaxTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, columns: list):
        self.columns = columns
        self.scaler = MinMaxScaler()

    def fit(self, X: pd.DataFrame, y=None):
        self.scaler.fit(X[self.columns])
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X_copy = X.copy()
        X_copy[self.columns] = self.scaler.transform(X_copy[self.columns])
        return X_copy
