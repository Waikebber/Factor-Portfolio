import time
from datetime import datetime
from typing import List, Optional, Dict, Any
import pandas as pd
from tqdm import tqdm
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent.parent))
from endpoints.FMPEndpoint import FMPEndpoint

class DataFetcher:
    def __init__(self, max_retries: int = 3, retry_delay: int = 30, batch_size: int = 25, batch_delay: int = 60):
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.batch_size = batch_size
        self.batch_delay = batch_delay
        self.fetcher = FMPEndpoint()

    def get_sp500_tickers(self) -> List[str]:
        url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        tables = pd.read_html(url)
        df = tables[0]
        return df['Symbol'].tolist()

    def download_with_retry(self, tickers: List[str], start_date: datetime, end_date: str) -> Optional[pd.DataFrame]:
        for attempt in range(self.max_retries):
            try:
                if attempt > 0:
                    print(f"Retry {attempt + 1} in {self.retry_delay} seconds...")
                    time.sleep(self.retry_delay)
                result = self._download_helper(tickers, start_date, end_date)
                if result is not None:
                    return result
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
        return None
    
    def _download_helper(self, tickers: List[str], start_date: datetime, end_date: str) -> Optional[pd.DataFrame]:
        for ticker in tickers:
            try:
                # Get analyst estimates for annual period
                analyst_estimates = self.fetcher.get_analyst_estimates(ticker, period="annual")
                if analyst_estimates:
                    print(f"Analyst estimates for {ticker}: {analyst_estimates}")
                    return pd.DataFrame(analyst_estimates)
                return None
            except Exception as e:
                print(f"Error fetching analyst estimates for {ticker}: {e}")
        return None

    def get_fundamental_data_with_retry(self, ticker: str) -> Optional[Dict[str, Any]]:
        for attempt in range(self.max_retries):
            try:
                if attempt > 0:
                    print(f"Retry {attempt + 1} for fundamentals...")
                    time.sleep(self.retry_delay)
                
                # Get fundamental data
                fundamental_data = self.fetcher.fetch(ticker)
                
                # Get economic indicators
                economic_indicators = self.fetcher.get_selected_economic_indicators()
                
                # Combine the data
                if fundamental_data:
                    fundamental_data["economic_indicators"] = economic_indicators
                    return fundamental_data
                return None
            except Exception as e:
                print(f"Fundamental data fetch failed for {ticker}: {e}")
        return None

    def process_batch(self, tickers: List[str], start_date: datetime, end_date: datetime,
                     store_factors, store_prices, store_estimates, store_macro) -> bool:
        try:
            price_data = self.download_with_retry(tickers, start_date, end_date)
            if price_data is None or price_data.empty:
                print("Price data is empty, skipping batch.")
                return False

            for ticker in tickers:
                if ticker not in price_data.columns:
                    continue

                adj_close = price_data[ticker].dropna()
                price_dict = {date.strftime('%Y-%m-%d'): float(value) for date, value in adj_close.items()}
                store_prices.store_daily_prices(ticker, price_dict)

                fund = self.get_fundamental_data_with_retry(ticker)
                if fund:
                    date = datetime.now().strftime('%Y-%m-%d')
                    store_factors.store_fundamental_ratios(ticker, date, fund)
                    store_factors.store_profitability(ticker, date, fund)
                    store_factors.store_liquidity_solvent_efficiency(ticker, date, fund)
                    store_factors.store_analyst_ratings(ticker, date, fund)
                    store_factors.store_technical_indicators(ticker, date, fund)
                    store_estimates.store_eps_revenue(ticker, date, fund)

                    macro_fields = [
                        ("cpi", "cpi.value", "cpi.date"),
                        ("gdp", "gdp.value", "gdp.date"),
                        ("unemploymentrate", "unemploymentrate.value", "unemploymentrate.date"),
                        ("federalfunds", "federalfunds.value", "federalfunds.date"),
                        ("30yearfixedratemortgageaverage", "30yearfixedratemortgageaverage.value", "30yearfixedratemortgageaverage.date")
                    ]
                    for macro_name, value_key, date_key in macro_fields:
                        value = fund.get(value_key)
                        macro_date = fund.get(date_key)
                        if value is not None and macro_date is not None:
                            if "rate" in macro_name:
                                store_macro.store_rate(macro_name, macro_date, value)
                            else:
                                store_macro.store_economic_indicator(macro_name, macro_date, value)

            return True
        except Exception as e:
            print(f"Error processing batch: {e}")
            return False 