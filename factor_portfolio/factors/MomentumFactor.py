"""
Momentum factor implementation.
"""

import pandas as pd
from .BaseFactor import Factor

class MomentumFactor(Factor):
    """Momentum factor based on trailing returns"""
    def compute(self, price_data, fundamental_data):
        """Compute momentum factor scores using trailing returns.
        
        Args:
            price_data (pd.DataFrame): Historical price data
            fundamental_data (pd.DataFrame): Fundamental data
            
        Returns:
            pd.Series: Momentum factor scores
        """
        # 12-month return minus 1-month return
        returns_12m = price_data.pct_change(252)
        returns_1m = price_data.pct_change(21)
        return pd.Series(returns_12m.iloc[-1] - returns_1m.iloc[-1], index=price_data.columns) 