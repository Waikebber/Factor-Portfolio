"""
Volatility factor implementation.
"""

import pandas as pd
from .base import Factor

class VolatilityFactor(Factor):
    """Volatility factor based on rolling standard deviation"""
    def compute(self, price_data, fundamental_data):
        """Compute volatility factor scores using rolling standard deviation.
        
        Args:
            price_data (pd.DataFrame): Historical price data
            fundamental_data (pd.DataFrame): Fundamental data
            
        Returns:
            pd.Series: Volatility factor scores
        """
        # 60-day rolling volatility
        returns = price_data.pct_change()
        vol = returns.rolling(60).std()
        return pd.Series(-vol.iloc[-1], index=price_data.columns)  # Negative because we want low volatility 