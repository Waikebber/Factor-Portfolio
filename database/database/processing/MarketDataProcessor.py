from .BaseProcessor import BaseProcessor
from ..translators.MarketDataTranslator import MarketDataTranslator

class MarketDataProcessor(BaseProcessor):
    def __init__(self, data_fetcher):
        super().__init__(data_fetcher.config)
        self.data_fetcher = data_fetcher

    def process_prices(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='prices',
            fetch_fn=lambda: self.data_fetcher.get_price_volume_data(
                ticker,
                from_date=start_date,
                to_date=end_date
            ),
            translate_fn=MarketDataTranslator.translate_prices,
            label="prices"
        )

    def process_dividend_adjusted_prices(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='dividend_adjusted_prices',
            fetch_fn=lambda: self.data_fetcher.get_dividend_adjusted_prices(
                ticker,
                from_date=start_date,
                to_date=end_date
            ),
            translate_fn=MarketDataTranslator.translate_dividend_adjusted_price,
            label="dividend adjusted prices"
        )

    def process_dividends(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='dividends',
            fetch_fn=lambda: self.data_fetcher.get_dividends(
                ticker,
                limit=self.config.dividends['limit']
            ),
            translate_fn=MarketDataTranslator.translate_dividends,
            label="dividends"
        )

    def process_splits(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='splits',
            fetch_fn=lambda: self.data_fetcher.get_splits(
                ticker,
                limit=self.config.splits['limit']
            ),
            translate_fn=MarketDataTranslator.translate_splits,
            label="splits"
        )

    def process_market_cap(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='market_cap',
            fetch_fn=lambda: self.data_fetcher.get_historical_market_cap(
                ticker,
                limit=self.config.market_cap['limit'],
                from_date=start_date,
                to_date=end_date
            ),
            translate_fn=MarketDataTranslator.translate_market_cap,
            label="market cap"
        )

    def process_share_float(self, ticker, start_date=None, end_date=None):
        return self.process_generic(
            ticker,
            start_date,
            end_date,
            config_key='general',
            fetch_fn=lambda: self.data_fetcher.get_share_float(ticker),
            translate_fn=MarketDataTranslator.translate_share_float,
            label="share float"
        ) 
    
    