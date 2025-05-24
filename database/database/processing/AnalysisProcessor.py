from .BaseProcessor import BaseProcessor
from ..translators.AnalysisTranslator import AnalysisTranslator

class AnalysisProcessor(BaseProcessor):
    def __init__(self, data_fetcher):
        super().__init__(data_fetcher.config)
        self.data_fetcher = data_fetcher

    def process_analyst_estimates(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='analyst_estimates',
            fetch_fn=lambda: self.data_fetcher.get_analyst_estimates(
                ticker,
                period=self.config.analyst_estimates['period'],
                page=self.config.analyst_estimates['page'],
                limit=self.config.analyst_estimates['limit']
            ),
            translate_fn=AnalysisTranslator.translate_analyst_estimates,
            label="analyst estimates"
    )


    def process_ratings(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='ratings',
            fetch_fn=lambda: self.data_fetcher.get_ratings(
                ticker,
                limit=self.config.ratings['limit']
            ),
            translate_fn=AnalysisTranslator.translate_ratings,
            label="ratings"
        )