import pandas as pd
import yaml

def load_yaml_config(path: str) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)

def compute_cagr(series: pd.Series) -> float:
    start_val = series.iloc[0]
    end_val = series.iloc[-1]
    n_years = (series.index[-1] - series.index[0]).days / 365.25
    return (end_val / start_val) ** (1 / n_years) - 1

def compute_sharpe(returns: pd.Series, risk_free_rate: float = 0.0) -> float:
    excess_returns = returns - risk_free_rate
    return (excess_returns.mean() / excess_returns.std()) * (12 ** 0.5)

def compute_drawdown(cumulative_returns: pd.Series) -> pd.Series:
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak
    return drawdown
