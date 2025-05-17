"""
Main script for running the factor investing portfolio.
"""

from datetime import datetime, timedelta
import pandas as pd
from factor_portfolio.utils.data_preparation import get_sp500_tickers, download_data
from factor_portfolio.utils.visualization import plot_results
from factor_portfolio.factors.value import ValueFactor
from factor_portfolio.factors.momentum import MomentumFactor
from factor_portfolio.factors.volatility import VolatilityFactor
from factor_portfolio.factors.size import SizeFactor
from factor_portfolio.backtesting.backtester import Backtester
import numpy as np

def calculate_metrics(returns):
    """Calculate performance metrics.
    
    Args:
        returns (pd.Series): Portfolio returns
        
    Returns:
        dict: Performance metrics
    """
    annual_return = returns.mean() * 252
    annual_vol = returns.std() * np.sqrt(252)
    sharpe_ratio = annual_return / annual_vol
    max_drawdown = (returns.cumsum() - returns.cumsum().cummax()).min()
    
    return {
        'Annual Return': annual_return,
        'Annual Volatility': annual_vol,
        'Sharpe Ratio': sharpe_ratio,
        'Maximum Drawdown': max_drawdown
    }

def main():
    """Main function to run the factor investing portfolio."""
    # Set date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365*3)  # 3 years of data

    # Get S&P 500 tickers and download data
    print("Downloading S&P 500 data...")
    tickers = get_sp500_tickers()
    price_data, fundamental_data = download_data(tickers, start_date, end_date)

    # Calculate returns
    returns = price_data.pct_change().dropna()

    # Initialize factors
    print("Computing factor scores...")
    factors = {
        'value': ValueFactor(),
        'momentum': MomentumFactor(),
        'volatility': VolatilityFactor(),
        'size': SizeFactor()
    }

    # Compute factor scores
    factor_scores = {}
    for name, factor in factors.items():
        factor_scores[name] = factor.compute(price_data, fundamental_data)

    # Combine factor scores into a DataFrame
    factor_df = pd.DataFrame(factor_scores)

    # Run backtest
    print("Running backtest...")
    backtester = Backtester(price_data, factor_df, returns)
    portfolio_returns = backtester.run()

    # Calculate and display metrics
    print("\nPortfolio Performance Metrics:")
    metrics = calculate_metrics(portfolio_returns)
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")

    # Plot results
    print("\nGenerating plots...")
    plot_results(portfolio_returns, factor_df, backtester)

if __name__ == "__main__":
    main() 