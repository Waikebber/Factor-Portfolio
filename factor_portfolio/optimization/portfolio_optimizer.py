"""
Portfolio optimization implementation.
"""

import pandas as pd
import cvxpy as cp

class PortfolioOptimizer:
    """Portfolio optimization using CVXPY"""
    def __init__(self, expected_returns, covariance_matrix):
        """Initialize portfolio optimizer.
        
        Args:
            expected_returns (pd.Series): Expected returns for each asset
            covariance_matrix (pd.DataFrame): Covariance matrix of returns
        """
        self.expected_returns = expected_returns
        self.covariance_matrix = covariance_matrix
        self.n_assets = len(expected_returns)
    
    def optimize_sharpe(self, risk_free_rate=0.02):
        """Maximize Sharpe ratio.
        
        Args:
            risk_free_rate (float): Risk-free rate
            
        Returns:
            pd.Series: Optimal portfolio weights
        """
        weights = cp.Variable(self.n_assets)
        returns = self.expected_returns @ weights
        risk = cp.quad_form(weights, self.covariance_matrix)
        
        # Constraints
        constraints = [
            cp.sum(weights) == 1,  # Full investment
            weights >= 0,  # Long-only
            weights <= 0.1  # Position limits
        ]
        
        # Objective: Maximize Sharpe ratio
        objective = cp.Maximize((returns - risk_free_rate) / cp.sqrt(risk))
        
        # Solve
        problem = cp.Problem(objective, constraints)
        problem.solve()
        
        return pd.Series(weights.value, index=self.expected_returns.index) 