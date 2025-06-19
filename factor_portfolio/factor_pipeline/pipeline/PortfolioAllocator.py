import pandas as pd

class PortfolioAllocator:
    """
    Utility to generate portfolio weights from factor scores.
    """

    def __init__(self, df: pd.DataFrame, score_col: str = "value_score"):
        self.df = df
        self.score_col = score_col

    def allocate(self, method: str = "equal", top_quantile: float = 0.2) -> pd.DataFrame:
        df = self.df.copy()
        df["rank"] = df.groupby("date")[self.score_col].rank(ascending=False, pct=True)
        df["selected"] = df["rank"] <= top_quantile

        if method == "equal":
            df["weight"] = df.groupby("date")["selected"].transform(lambda x: 1 / x.sum()) * df["selected"]
        elif method == "score":
            df["weight"] = df[self.score_col] * df["selected"]
            df["weight"] /= df.groupby("date")["weight"].transform("sum")
        else:
            raise ValueError("Unsupported allocation method: choose 'equal' or 'score'")

        return df[["date", "symbol", self.score_col, "weight"]]
