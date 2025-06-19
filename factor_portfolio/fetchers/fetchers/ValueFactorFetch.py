from fetchers.fetchers.BaseFetcher import BaseFetcher
import pandas as pd
from typing import Union, List
from dateutil.relativedelta import relativedelta

class ValueFactorFetch(BaseFetcher):
    def __init__(self, config: dict = None):
        super().__init__(config=config)

    def fetch(self, symbol: Union[str, List[str]], start_date: str = None, end_date: str = None) -> pd.DataFrame:
        start_date = pd.to_datetime(start_date or self.default_start_date)
        end_date = pd.to_datetime(end_date or self.default_end_date)
        symbols = [symbol] if isinstance(symbol, str) else symbol

        prices = self._fetch_prices(symbols, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))
        data_sources_start_date = (start_date - relativedelta(years=1)).strftime("%Y-%m-%d")
        data_sources = self._fetch_all_data_sources(symbols, data_sources_start_date, end_date.strftime("%Y-%m-%d"))
        market_cap_df = self._fetch_market_cap(symbols, data_sources_start_date, end_date.strftime("%Y-%m-%d"))

        combined_df = self._combine_data_sources(prices, data_sources, market_cap_df)
        combined_df = combined_df.reset_index()
        mask = (combined_df['date'] >= start_date) & (combined_df['date'] <= end_date)
        combined_df = combined_df[mask].set_index(["symbol", "date"])

        if combined_df.empty:
            raise ValueError("No data available after combining all sources")
        return combined_df


    def _fetch_prices(self, symbols: List[str], start_date: str, end_date: str) -> pd.DataFrame:
        # Include 1 day prior to ensure the first row has prior price
        padded_start = (pd.to_datetime(start_date) - pd.Timedelta(days=1)).strftime("%Y-%m-%d")
        prices = self.getter.market_data.get_price_data(symbols, padded_start, end_date, ["symbol", "date", "close"])
        if not prices:
            raise ValueError(f"No prices data found for {symbols}")
        prices_df = pd.DataFrame(prices)
        prices_df["date"] = pd.to_datetime(prices_df["date"])
        return prices_df
    
    def _fetch_market_cap(self, symbols, start_date, end_date):
        raw = self.getter.market_data.get_market_cap(
            symbols,
            (pd.to_datetime(start_date) - pd.Timedelta(days=5)).strftime("%Y-%m-%d"),
            end_date,
            ["symbol", "date", "market_cap"]
        )
        mc = pd.DataFrame(raw)
        if mc.empty:
            return mc
        mc["date"] = pd.to_datetime(mc["date"])
        mc = mc.sort_values(["date", "symbol"])   # date PRIMARY, symbol SECONDARY

        prices = self._fetch_prices(symbols, start_date, end_date)
        calendar = (
            prices[["symbol", "date"]]
            .drop_duplicates()
            .assign(date=lambda df: pd.to_datetime(df["date"]))
            .sort_values(["date", "symbol"])        # same ordering!
        )

        merged = pd.merge_asof(
            calendar,
            mc,
            on="date",
            by="symbol",
            direction="backward",
            allow_exact_matches=True
        )
        return merged[["symbol", "date", "market_cap"]]

    def _fetch_all_data_sources(self, symbols: List[str], start_date: str, end_date: str) -> List[pd.DataFrame]:
        sources = [
            self.getter.financial_metrics.get_earnings(symbols, start_date, end_date, ["symbol", "date", "eps_actual"]),
            self.getter.financial_metrics.get_key_metrics(symbols, start_date, end_date, [
                "symbol", "date", "earnings_yield", "free_cash_flow_yield", "graham_number", 
                "return_on_equity", "return_on_assets", "enterprise_value"
            ]),
            self.getter.financial_metrics.get_financial_ratios(symbols, start_date, end_date, [
                "symbol", "date", "price_to_earnings_ratio", "price_to_book_ratio",
                "price_to_sales_ratio", "price_to_free_cash_flow_ratio"
            ]),
            self.getter.valuation.get_enterprise_values(symbols, start_date, end_date, [
                "symbol", "date", "enterprise_value"
            ])
        ]
        dfs = [pd.DataFrame(df) for df in sources if df]

        if len(dfs) >= 2 and not dfs[1].empty and not dfs[0].empty:
            dfs[1] = self._clean_null_graham_number(dfs[1], dfs[0])
        for df in dfs:
            if not df.empty:
                df["date"] = pd.to_datetime(df["date"])
        if len(dfs) >= 4 and "enterprise_value" in dfs[3].columns:
            dfs[3] = dfs[3].drop(columns=["enterprise_value"])
        return dfs
    
    def _combine_data_sources(self, prices, data_sources, market_cap_df=None):
        df = prices.set_index(["symbol", "date"])
        for src in data_sources:
            if src.empty:
                continue
            aligned = self.expand_periodic_data(prices, src)
            aligned = aligned.drop(columns=["close"], errors="ignore")
            overlap = df.columns.intersection(aligned.columns)
            if len(overlap):
                aligned = aligned.drop(columns=overlap)
            df = df.join(aligned, how="left")

        if market_cap_df is not None and not market_cap_df.empty:
            mc_idx = market_cap_df.set_index(["symbol", "date"])
            df = df.join(mc_idx, how="left")
        df = df.groupby(level=0).ffill().bfill()
        return df
    
    def _clean_null_graham_number(self, key_metrics_df: pd.DataFrame, earnings_df: pd.DataFrame) -> pd.DataFrame:
        missing_rows = key_metrics_df[key_metrics_df["graham_number"].isnull()]
        if missing_rows.empty:
            return key_metrics_df

        symbols = missing_rows["symbol"].unique().tolist()
        missing_rows = missing_rows.copy()
        missing_rows["date"] = pd.to_datetime(missing_rows["date"])
        start_date = missing_rows["date"].min().strftime("%Y-%m-%d")
        end_date = missing_rows["date"].max().strftime("%Y-%m-%d")

        # Fetch book value per share
        bvps_raw = self.getter.financial_metrics.get_financial_ratios(
            symbols,
            start_date,
            end_date,
            ["symbol", "date", "book_value_per_share"]
        )
        bvps_df = pd.DataFrame(bvps_raw)
        if bvps_df.empty or "symbol" not in bvps_df.columns:
            return key_metrics_df
        bvps_df["date"] = pd.to_datetime(bvps_df["date"])

        # Make sure earnings_df is usable
        earnings_df = earnings_df.copy()
        earnings_df["date"] = pd.to_datetime(earnings_df["date"])

        # Merge all required data
        merged = pd.merge(missing_rows, earnings_df, on=["symbol", "date"], how="inner")
        merged = pd.merge(merged, bvps_df, on=["symbol", "date"], how="inner")

        # Compute and fill graham_number
        merged["graham_number_filled"] = (22.5 * merged["eps_actual"] * merged["book_value_per_share"]) ** 0.5
        
        # Ensure key_metrics_df date column is datetime before merging
        key_metrics_df = key_metrics_df.copy()
        key_metrics_df["date"] = pd.to_datetime(key_metrics_df["date"])
        
        key_metrics_df = key_metrics_df.merge(
            merged[["symbol", "date", "graham_number_filled"]],
            on=["symbol", "date"],
            how="left"
        )
        key_metrics_df["graham_number"] = key_metrics_df["graham_number"].fillna(key_metrics_df["graham_number_filled"])
        key_metrics_df.drop(columns=["graham_number_filled"], inplace=True)

        return key_metrics_df.dropna(subset=["graham_number"])
