"""
Backtesting framework implementation.
"""

import pandas as pd
from ..models.alpha_model import AlphaModel
from ..optimization.portfolio_optimizer import PortfolioOptimizer
from ..optimization.risk_model import RiskModel
from ..utils.data_preparation import prepare_alpha_data

class Backtester:
    """Backtesting framework"""
    def __init__(self, price_data, factor_df, returns, rebalance_freq=21):
        """Initialize backtester.
        
        Args:
            price_data (pd.DataFrame): Historical price data
            factor_df (pd.DataFrame): Factor scores
            returns (pd.DataFrame): Asset returns
            rebalance_freq (int): Rebalancing frequency in days
        """
        self.price_data = price_data
        self.factor_df = factor_df
        self.returns = returns
        self.rebalance_freq = rebalance_freq
        self.portfolio_returns = []
        self.weights_history = []
    
    def run(self):
        """Run backtest.
        
        Returns:
            pd.Series: Portfolio returns
        """
        dates = self.returns.index[252:]  # Start after initial lookback
        
        for i in range(0, len(dates), self.rebalance_freq):
            current_date = dates[i]
            
            # Get data up to current date
            lookback_returns = self.returns.loc[:current_date]
            lookback_factors = self.factor_df.loc[:current_date]
            
            # Train alpha model
            X_train, _, y_train, _ = prepare_alpha_data(lookback_factors, lookback_returns)
            alpha_model = AlphaModel()
            alpha_model.fit(X_train, y_train)
            
            # Generate predictions
            current_factors = lookback_factors.iloc[-1:]
            predictions = alpha_model.predict(current_factors)
            
            # Compute covariance
            risk_model = RiskModel(lookback_returns)
            cov_matrix = risk_model.compute_covariance().iloc[-1]
            
            # Optimize portfolio
            optimizer = PortfolioOptimizer(pd.Series(predictions[0], index=current_factors.columns), cov_matrix)
            weights = optimizer.optimize_sharpe()
            
            # Store weights
            self.weights_history.append(weights)
            
            # Calculate portfolio returns
            if i + self.rebalance_freq < len(dates):
                period_returns = self.returns.loc[current_date:dates[i + self.rebalance_freq]]
                portfolio_return = (period_returns * weights).sum(axis=1)
                self.portfolio_returns.extend(portfolio_return)
        
        return pd.Series(self.portfolio_returns, index=dates[:len(self.portfolio_returns)]) 