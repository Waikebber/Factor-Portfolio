from .BaseProcessor import BaseProcessor
from ..translators.GrowthTranslator import GrowthTranslator

class GrowthProcessor(BaseProcessor):
    def __init__(self, data_fetcher):
        super().__init__(data_fetcher.config)
        self.data_fetcher = data_fetcher

    def process_financial_statement_growth(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='financial_statement_growth',
            fetch_fn=lambda: self.data_fetcher.get_financial_statement_growth(
                ticker,
                limit=self.config.financial_statement_growth['limit'],
                period=self.config.financial_statement_growth['period']
            ),
            translate_fn=GrowthTranslator.translate_financial_statement_growth,
            label="financial statement growth"
        )

    def process_income_statement_growth(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='income_statement_growth',
            fetch_fn=lambda: self.data_fetcher.get_income_statement_growth(
                ticker,
                limit=self.config.income_statement_growth['limit'],
                period=self.config.income_statement_growth['period']
            ),
            translate_fn=GrowthTranslator.translate_income_statement_growth,
            label="income statement growth"
        )

    def process_balance_sheet_growth(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='balance_sheet_growth',
            fetch_fn=lambda: self.data_fetcher.get_balance_sheet_growth(
                ticker,
                limit=self.config.balance_sheet_growth['limit'],
                period=self.config.balance_sheet_growth['period']
            ),
            translate_fn=GrowthTranslator.translate_balance_sheet_growth,
            label="balance sheet growth"
        )

    def process_cashflow_statement_growth(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='cashflow_statement_growth',
            fetch_fn=lambda: self.data_fetcher.get_cashflow_statement_growth(
                ticker,
                limit=self.config.cashflow_statement_growth['limit'],
                period=self.config.cashflow_statement_growth['period']
            ),
            translate_fn=GrowthTranslator.translate_cashflow_statement_growth,
            label="cashflow statement growth"
        ) 