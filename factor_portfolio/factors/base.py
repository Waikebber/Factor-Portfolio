"""
Base Factor class for factor computation.
"""

class Factor:
    """Base class for factor computation"""
    def compute(self, price_data, fundamental_data):
        """Compute factor scores.
        
        Args:
            price_data (pd.DataFrame): Historical price data
            fundamental_data (pd.DataFrame): Fundamental data
            
        Returns:
            pd.Series: Factor scores
        """
        raise NotImplementedError 