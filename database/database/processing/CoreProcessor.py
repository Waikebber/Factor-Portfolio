from typing import Dict, Any, List, Optional
from .BaseProcessor import BaseProcessor
from ..translators.CoreTranslator import CoreTranslator
from ..data_fetchers.FMPFetcher import FMPFetcher

class CoreProcessor(BaseProcessor):
    def __init__(self, data_fetcher: FMPFetcher):
        super().__init__(data_fetcher.config)
        self.data_fetcher = data_fetcher

    def process_stocks(self, ticker: str, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='general',
            fetch_fn=lambda: self.data_fetcher.get_stocks(ticker),
            translate_fn=CoreTranslator.translate_stocks,
            label='stocks'
        )

    def process_employee_count(self, ticker: str, start_date: Optional[str] = None, end_date: Optional[str] = None) -> Optional[List[Dict[str, Any]]]:
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='employee_count',
            fetch_fn=lambda: self.data_fetcher.get_historical_employee_count(
                ticker,
                limit=self.config.employee_count['limit']
            ),
            translate_fn=CoreTranslator.translate_employee_count,
            label='employee count'
        )
