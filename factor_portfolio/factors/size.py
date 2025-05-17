"""
Size factor implementation.
"""

import numpy as np
import pandas as pd
from .base import Factor

class SizeFactor(Factor):
    """Size factor based on market capitalization"""
    def compute(self, price_data, fundamental_data):
        """Compute size factor scores using market capitalization.
        
        Args:
            price_data (pd.DataFrame): Historical price data
            fundamental_data (pd.DataFrame): Fundamental data
            
        Returns:
            pd.Series: Size factor scores
        """
        # Log of market cap
        return pd.Series(-np.log(fundamental_data['market_cap']), index=fundamental_data.index)  # Negative because we want small cap 