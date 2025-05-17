"""
Value factor implementation.
"""

import numpy as np
from .base import Factor
import pandas as pd

class ValueFactor(Factor):
    """Value factor based on P/E and P/B ratios"""
    def compute(self, price_data, fundamental_data):
        """Compute value factor scores using P/E and P/B ratios.
        
        Args:
            price_data (pd.DataFrame): Historical price data
            fundamental_data (pd.DataFrame): Fundamental data
            
        Returns:
            pd.Series: Value factor scores
        """
        # Inverse of P/E and P/B ratios
        pe_factor = 1 / fundamental_data['pe_ratio']
        pb_factor = 1 / fundamental_data['pb_ratio']
        return pd.Series((pe_factor + pb_factor) / 2, index=fundamental_data.index) 