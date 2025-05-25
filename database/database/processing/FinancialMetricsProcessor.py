from .BaseProcessor import BaseProcessor
from ..translators.FinancialMetricsTranslator import FinancialMetricsTranslator

class FinancialMetricsProcessor(BaseProcessor):
    def __init__(self, data_fetcher):
        super().__init__(data_fetcher.config)
        self.data_fetcher = data_fetcher

    def process_key_metrics(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='key_metrics',
            fetch_fn=lambda: self.data_fetcher.get_key_metrics(
                ticker,
                limit=self.config.key_metrics['limit'],
                period=self.config.key_metrics['period']
            ),
            translate_fn=FinancialMetricsTranslator.translate_key_metrics,
            label="key metrics"
        )

    def process_financial_ratios(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='financial_ratios',
            fetch_fn=lambda: self.data_fetcher.get_financial_ratios(
                ticker,
                limit=self.config.financial_ratios['limit'],
                period=self.config.financial_ratios['period']
            ),
            translate_fn=FinancialMetricsTranslator.translate_financial_ratios,
            label="financial ratios"
        )
    
    def process_earnings(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='earnings',
            fetch_fn=lambda: self.data_fetcher.get_earnings(
                ticker,
                limit=self.config.earnings['limit']
            ),
            translate_fn=FinancialMetricsTranslator.translate_earnings,
            label="earnings"
        )