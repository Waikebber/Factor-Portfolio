from .BaseFetcher import BaseFetcher
import pandas as pd

class ValueFactorFetch(BaseFetcher):
    def __init__(self, config: dict = None):
        super().__init__(config=config)

    def fetch(self, symbol: str, start_date: str = None, end_date: str = None) -> pd.DataFrame:
        start_date = start_date or self.default_start_date
        end_date = end_date or self.default_end_date

        prices = self.getter.market_data.get_prices(symbol, start_date, end_date)[["symbol", "date", "close"]]
        market_cap = self.getter.market_data.get_market_cap(symbol, start_date, end_date)[["symbol", "date", "market_cap"]]
        earnings = self.getter.valuation.get_earnings(symbol, start_date, end_date)[["symbol", "date", "eps_actual"]]
        key_metrics = self.getter.financial_metrics.get_key_metrics(symbol, start_date, end_date)[[
            "symbol", "date", "book_value_per_share", "free_cash_flow_yield", "earnings_yield"
        ]]
        financial_ratios = self.getter.financial_metrics.get_financial_ratios(symbol, start_date, end_date)[[
            "symbol", "date", "price_to_earnings_ratio", "price_to_book_ratio",
            "price_to_sales_ratio", "price_to_free_cash_flow_ratio"
        ]]
        enterprise_values = self.getter.valuation.get_enterprise_values(symbol, start_date, end_date)[[
            "symbol", "date", "enterprise_value"
        ]]

        dfs = [prices, market_cap, earnings, key_metrics, financial_ratios, enterprise_values]
        for df in dfs:
            df.set_index(["symbol", "date"], inplace=True)

        combined = pd.concat(dfs, axis=1)

        if self.clean_missing:
            combined.dropna(inplace=True)

        if self.frequency:
            combined = (
                combined.groupby("symbol")
                .resample(self.frequency, level="date")
                .last()
                .dropna(how="all")
                .reset_index()
            )
        else:
            combined.reset_index(inplace=True)

        return combined

