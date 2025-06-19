import pandas as pd

class Backtester:
    """
    Simple backtester to track portfolio performance using factor scores.
    """

    def __init__(self, df: pd.DataFrame, score_col: str = "value_score", return_col: str = "next_return"):
        self.df = df.copy()
        self.score_col = score_col
        self.return_col = return_col

    def run(self, top_quantile: float = 0.2, weight_type: str = "equal") -> pd.Series:
        df = self.df.copy()
        df["rank"] = df.groupby("date")[self.score_col].rank(ascending=False, pct=True)
        df["selected"] = df["rank"] <= top_quantile

        if weight_type == "equal":
            df["weight"] = df.groupby("date")["selected"].transform(lambda x: 1 / x.sum()) * df["selected"]
        elif weight_type == "score":
            df["weight"] = df[self.score_col] * df["selected"]
            df["weight"] /= df.groupby("date")["weight"].transform("sum")
        else:
            raise ValueError("weight_type must be 'equal' or 'score'")

        df["weighted_return"] = df["weight"] * df[self.return_col]
        monthly_return = df.groupby("date")["weighted_return"].sum()
        cumulative = (1 + monthly_return).cumprod()
        return cumulative
