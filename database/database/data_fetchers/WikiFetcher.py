from typing import List
from endpoints.WikiEndpoint import WikiEndpoint

class WikiFetcher:
    def __init__(self):
        self.endpoint = WikiEndpoint()
    
    def get_sp500_tickers(self) -> List[str]:
        """Fetch S&P 500 tickers from Wikipedia"""
        return self.endpoint.get_sp500_tickers()