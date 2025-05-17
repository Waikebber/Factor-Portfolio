"""
Visualization utilities.
"""

import matplotlib.pyplot as plt
import seaborn as sns

def plot_results(portfolio_returns, factor_df, backtester):
    """Plot portfolio performance and analysis.
    
    Args:
        portfolio_returns (pd.Series): Portfolio returns
        factor_df (pd.DataFrame): Factor scores
        backtester (Backtester): Backtester instance
    """
    # Plot cumulative returns
    plt.figure(figsize=(12, 6))
    cumulative_returns = (1 + portfolio_returns).cumprod()
    plt.plot(cumulative_returns.index, cumulative_returns.values)
    plt.title('Cumulative Portfolio Returns')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.grid(True)
    plt.show()

    # Plot factor exposures
    plt.figure(figsize=(12, 6))
    factor_df.mean().plot(kind='bar')
    plt.title('Average Factor Exposures')
    plt.xlabel('Factor')
    plt.ylabel('Exposure')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

    # Plot portfolio weights
    plt.figure(figsize=(12, 6))
    latest_weights = backtester.weights_history[-1]
    latest_weights.sort_values(ascending=False).head(10).plot(kind='bar')
    plt.title('Top 10 Portfolio Weights')
    plt.xlabel('Asset')
    plt.ylabel('Weight')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show() 