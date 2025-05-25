from .BaseProcessor import BaseProcessor
from ..translators.AnalystDataTranslator import AnalystDataTranslator

class AnalystDataProcessor(BaseProcessor):
    def __init__(self, data_fetcher):
        super().__init__(data_fetcher.config)
        self.data_fetcher = data_fetcher

    def process_grades(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='grades',
            fetch_fn=lambda: self.data_fetcher.get_grades_historical(
                ticker,
                limit=self.config.grades['limit']
            ),
            translate_fn=AnalystDataTranslator.translate_grades,
            label="grades"
        )

    def process_grades_consensus(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='general',
            fetch_fn=lambda: self.data_fetcher.get_grades_consensus(ticker),
            translate_fn=AnalystDataTranslator.translate_grades_consensus,
            label="grades consensus"
        )

    def process_price_target_consensus(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='general',
            fetch_fn=lambda: self.data_fetcher.get_price_target_consensus(ticker),
            translate_fn=AnalystDataTranslator.translate_price_target_consensus,
            label="price target consensus"
        )

    def process_price_target_summary(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='general',
            fetch_fn=lambda: self.data_fetcher.get_price_target_summary(ticker),
            translate_fn=AnalystDataTranslator.translate_price_target_summary,
            label="price target summary"
        )