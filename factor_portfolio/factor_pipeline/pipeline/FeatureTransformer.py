import pandas as pd
from scipy.stats import zscore

class FeatureTransformer:
    """
    Handles z-score normalization, winsorization, lagging, and feature engineering.
    """

    @staticmethod
    def zscore_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
        for col in columns:
            df["z_" + col] = df.groupby("date")[col].transform(zscore)
        return df

    @staticmethod
    def winsorize(df: pd.DataFrame, columns: list[str], lower: float = 0.01, upper: float = 0.99) -> pd.DataFrame:
        for col in columns:
            lower_val = df[col].quantile(lower)
            upper_val = df[col].quantile(upper)
            df[col] = df[col].clip(lower_val, upper_val)
        return df

    @staticmethod
    def lag_column(df: pd.DataFrame, group_col: str, column: str, lag: int = 1) -> pd.DataFrame:
        df[f"{column}_lag{lag}"] = df.groupby(group_col)[column].shift(lag)
        return df

    @staticmethod
    def compute_forward_return(df: pd.DataFrame, price_col: str = "close", horizon: int = 1) -> pd.DataFrame:
        df["next_return"] = df.groupby("symbol")[price_col].shift(-horizon) / df[price_col] - 1
        return df
