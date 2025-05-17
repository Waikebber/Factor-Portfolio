"""
Risk model implementation.
"""

import numpy as np
import pandas as pd

class RiskModel:
    """Risk model for portfolio optimization"""
    def __init__(self, returns, lookback=252):
        self.returns = returns
        self.lookback = lookback
    
    def compute_covariance(self):
        """Compute covariance matrix with shrinkage"""
        sample_cov = self.returns.rolling(self.lookback).cov().dropna()
        n = sample_cov.shape[0]
        shrinkage = 0.5
        avg_corr = sample_cov.mean().mean()
        prior = np.ones((n, n)) * avg_corr
        np.fill_diagonal(prior, 1)
        return shrinkage * prior + (1 - shrinkage) * sample_cov 