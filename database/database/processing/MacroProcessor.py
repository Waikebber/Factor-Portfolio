from .BaseProcessor import BaseProcessor
from ..translators.MacroTranslator import MacroTranslator

class MacroProcessor(BaseProcessor):
    def __init__(self, data_fetcher):
        super().__init__(data_fetcher.config)
        self.data_fetcher = data_fetcher

    def process_economic_indicators(self, start_date=None, end_date=None):
        return self.process_generic(
            None,
            start_date,
            end_date,
            config_key='economic_indicators',
            fetch_fn=lambda: self.data_fetcher.get_economic_indicators(
                name=None,
                from_date=start_date,
                to_date=end_date
            ),
            translate_fn=MacroTranslator.translate_economic_indicators,
            label="economic indicators"
        )


    def process_industry_pe(self, industry, start_date=None, end_date=None):
        return self.process_generic(
            None,
            start_date,
            end_date,
            config_key='industry_pe',
            fetch_fn=lambda: self.data_fetcher.get_historical_industry_pe(
                industry,
                from_date=start_date,
                to_date=end_date,
                exchange=self.config.industry_pe['exchange']
            ),
            translate_fn=MacroTranslator.translate_industry_pe,
            label="industry P/E"
        )

    def process_sector_pe(self, sector, start_date=None, end_date=None):
        return self.process_generic(
            None,
            start_date,
            end_date,
            config_key='sector_pe',
            fetch_fn=lambda: self.data_fetcher.get_historical_sector_pe(
                sector,
                from_date=start_date,
                to_date=end_date,
                exchange=self.config.sector_pe['exchange']
            ),
            translate_fn=MacroTranslator.translate_sector_pe,
            label="sector P/E"
        )

    def process_industry_performance(self, industry, start_date=None, end_date=None):
        return self.process_generic(
            None,
            start_date,
            end_date,
            config_key='industry_performance',
            fetch_fn=lambda: self.data_fetcher.get_historical_industry_performance(
                industry,
                from_date=start_date,
                to_date=end_date,
                exchange=self.config.industry_performance['exchange']
            ),
            translate_fn=MacroTranslator.translate_industry_performance,
            label="industry performance"
        )

    def process_sector_performance(self, sector, start_date=None, end_date=None):
        return self.process_generic(
            None,
            start_date,
            end_date,
            config_key='sector_performance',
            fetch_fn=lambda: self.data_fetcher.get_historical_sector_performance(
                sector,
                from_date=start_date,
                to_date=end_date,
                exchange=self.config.sector_performance['exchange']
            ),
            translate_fn=MacroTranslator.translate_sector_performance,
            label="sector performance"
        )

    def process_treasury_rates(self, start_date=None, end_date=None):
        return self.process_generic(
            None,
            start_date,
            end_date,
            config_key='treasury_rates',
            fetch_fn=lambda: self.data_fetcher.get_treasury_rates(
                from_date=start_date,
                to_date=end_date
            ),
            translate_fn=MacroTranslator.translate_treasury_rates,
            label="treasury rates"
        ) 
    
    def process_mergers_acquisitions(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='mergers_acquisitions',
            fetch_fn=lambda: self.data_fetcher.get_latest_mergers_acquisitions(
                page=self.config.mergers_acquisitions['page'],
                limit=self.config.mergers_acquisitions['limit']
            ),
            translate_fn=MacroTranslator.translate_mergers_acquisitions,
            label="mergers and acquisitions"
        ) 