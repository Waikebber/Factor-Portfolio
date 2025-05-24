import time
from datetime import datetime
from typing import List, Optional, Dict, Any
import pandas as pd
from endpoints.FMPEndpoint import FMPEndpoint
from ..config.data_fetch_config import DataFetchConfig

class FMPFetcher:
    def __init__(self, config: Optional[DataFetchConfig] = None):
        self.config = config or DataFetchConfig()
        self.fetcher = FMPEndpoint()
    
    def _with_retry(self, func, label: str):
        """Retry mechanism for API calls"""
        for attempt in range(self.config.max_retries):
            try:
                if attempt > 0:
                    print(f"Retry {attempt + 1} for {label}...")
                    time.sleep(self.config.retry_delay)
                return func()
            except Exception as e:
                print(f"Error on attempt {attempt + 1} for {label}: {e}")
                if attempt == self.config.max_retries - 1:
                    raise 

    def get_sp500_tickers(self) -> List[str]:
        """Fetch S&P 500 tickers from Wikipedia"""
        url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        tables = pd.read_html(url)
        df = tables[0]
        return df['Symbol'].tolist()

    def get_analyst_estimates(
        self,
        ticker: str,
        period: str,
        page: int,
        limit: int
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch raw analyst estimates from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_analyst_estimates(ticker, period, page, limit),
            f"analyst estimates for {ticker}"
        )

    def get_ratings(
        self,
        ticker: str,
        limit: int
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch raw ratings from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_ratings_historical(ticker, limit),
            f"ratings for {ticker}"
        )
    
