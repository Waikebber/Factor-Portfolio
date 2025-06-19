from .BaseFetcher import BaseFetcher
import pandas as pd

class SP500TickersFetcher(BaseFetcher):
    def __init__(self, config: dict = None):
        super().__init__(config=config)

    def fetch(self, symbol: str = None, start_date: str = None, end_date: str = None) -> pd.DataFrame:
        return self.getter.ticker

    def fetch_date(self, symbol: str = None, date: str = None) -> pd.DataFrame:
        raise NotImplementedError("TickerFetch does not support fetch_date")
    
    def expand_periodic_data(self, price_df: pd.DataFrame = None, periodic_df: pd.DataFrame = None) -> pd.DataFrame:
        raise NotImplementedError("TickerFetch does not support expand_periodic_data")
