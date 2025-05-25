from .BaseProcessor import BaseProcessor
from ..translators.ValuationTranslator import ValuationTranslator

class ValuationProcessor(BaseProcessor):
    def __init__(self, data_fetcher):
        super().__init__(data_fetcher.config)
        self.data_fetcher = data_fetcher

    def process_discounted_cash_flow(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='discounted_cash_flow',
            fetch_fn=lambda: self.data_fetcher.get_discounted_cash_flow(ticker),
            translate_fn=ValuationTranslator.translate_discounted_cash_flow,
            label="discounted cash flow"
        )

    def process_levered_discounted_cash_flow(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='levered_discounted_cash_flow',
            fetch_fn=lambda: self.data_fetcher.get_levered_discounted_cash_flow(ticker),
            translate_fn=ValuationTranslator.translate_levered_discounted_cash_flow,
            label="levered discounted cash flow"
        )

    def process_enterprise_values(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='enterprise_values',
            fetch_fn=lambda: self.data_fetcher.get_enterprise_values(
                ticker,
                limit=self.config.enterprise_values['limit'],
                period=self.config.enterprise_values['period']
            ),
            translate_fn=ValuationTranslator.translate_enterprise_values,
            label="enterprise values"
        )

    def process_owner_earnings(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='owner_earnings',
            fetch_fn=lambda: self.data_fetcher.get_owner_earnings(
                ticker,
                limit=self.config.owner_earnings['limit']
            ),
            translate_fn=ValuationTranslator.translate_owner_earnings,
            label="owner earnings"
        ) 