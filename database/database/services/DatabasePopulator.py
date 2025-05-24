from datetime import datetime, timedelta
import logging
import pandas as pd
from typing import Dict, Any, Optional, List
from ..StockDatabase import StockDatabase
from ..db_writers.StoreFactors import StoreFactors
from ..db_writers.StoreMarketData import StorePrices
from ..db_writers.StoreEstimates import StoreEstimates
from ..db_writers.StoreMacroData import StoreMacroData
from ..db_writers.StoreStocks import StoreStocks
from ..db_writers.DataFetcher import DataFetcher

class DatabasePopulator:
    """
    Service class responsible for orchestrating the database population process.
    Coordinates data fetching, transformation, and storage operations.
    """
    def __init__(self, db: StockDatabase):
        self.db = db
        self.data_fetcher = DataFetcher()
        conn = self.db._get_connection()
        self.store_factors = StoreFactors(conn)
        self.store_prices = StorePrices(conn)
        self.store_estimates = StoreEstimates(conn)
        self.store_macro = StoreMacroData(conn)
        self.store_stocks = StoreStocks(conn)
        logging.basicConfig(level=logging.INFO)

    def populate(self, tickers: Optional[List[str]] = None):
        """
        Populate the database with data for the specified tickers.
        If no tickers are provided, uses S&P 500 tickers.
        """
        if tickers is None:
            tickers = self.data_fetcher.get_sp500_tickers()
            logging.info(f"Using default tickers from S&P 500 ({len(tickers)} tickers)")
        else:
            logging.info(f"Populating data for provided tickers: {tickers}")

        self.populate_batch(tickers)

    def populate_batch(self, tickers: List[str]):
        """
        Process a batch of tickers sequentially.
        """
        for ticker in tickers:
            logging.info(f"Starting population for ticker: {ticker}")
            self.populate_one_ticker(ticker)

    def populate_one_ticker(self, ticker: str):
        """
        Populate data for a single ticker.
        """
        try:
            data = self._fetch_all_data(ticker)
            date = datetime.now().strftime('%Y-%m-%d')
            self._store_all_data(ticker, date, data)
            logging.info(f"Successfully populated data for ticker: {ticker}")
        except Exception as e:
            logging.error(f"Failed to populate {ticker}: {e}")

    def _fetch_all_data(self, ticker: str) -> Dict[str, Any]:
        """
        Fetch all required data for a ticker using the DataFetcher.
        """
        fundamentals = self.data_fetcher.get_fundamental_data_with_retry(ticker)
        prices = self.data_fetcher.download_with_retry([ticker],
                                              (datetime.now() - timedelta(days=365)),
                                              datetime.now())
        print("prices\n", prices)
        
        if prices is not None and ticker in prices.columns:
            # Convert price data to dictionary format
            price_data = {}
            for date, row in prices[ticker].iterrows():
                price_data[date.strftime('%Y-%m-%d')] = {
                    'open': float(row['open']) if pd.notna(row['open']) else None,
                    'high': float(row['high']) if pd.notna(row['high']) else None,
                    'low': float(row['low']) if pd.notna(row['low']) else None,
                    'close': float(row['close']) if pd.notna(row['close']) else None,
                    'adjOpen': float(row['adjOpen']) if pd.notna(row['adjOpen']) else None,
                    'adjHigh': float(row['adjHigh']) if pd.notna(row['adjHigh']) else None,
                    'adjLow': float(row['adjLow']) if pd.notna(row['adjLow']) else None,
                    'adjClose': float(row['adjClose']) if pd.notna(row['adjClose']) else None,
                    'volume': int(row['volume']) if pd.notna(row['volume']) else None,
                    'vwap': float(row['vwap']) if pd.notna(row['vwap']) else None,
                    'change': float(row['change']) if pd.notna(row['change']) else None,
                    'changePercent': float(row['changePercent']) if pd.notna(row['changePercent']) else None,
                    'changes': float(row['changes']) if pd.notna(row['changes']) else None,
                    'dividend': float(row['dividend']) if pd.notna(row['dividend']) else None,
                    'adj_dividend': float(row['adj_dividend']) if pd.notna(row['adj_dividend']) else None
                }
        else:
            price_data = {}

        return {**fundamentals, "price_data": price_data} if fundamentals else {"price_data": price_data}

    def _store_all_data(self, ticker: str, date: str, data: Dict[str, Any]):
        """
        Store all fetched data using appropriate database writers.
        """
        if not data:
            logging.warning(f"No data to store for {ticker}")
            return

        # Extract data from nested structure
        key_metrics = data.get("key_metrics", {})
        financial_ratios = data.get("financial_ratios", {})
        company_info = data.get("company_info", {})
        growth_metrics = data.get("growth_metrics", {})
        valuation = data.get("valuation", {})

        # Use the date from key_metrics if available, otherwise use current date
        effective_date = key_metrics.get("date", date)

        # Store company info
        self.store_stocks.store_stock_info(ticker, company_info, effective_date)

        # Store fundamentals
        self.store_factors.store_fundamental_ratios(ticker, effective_date, {
            **key_metrics,
            **financial_ratios,
            **company_info,
            **valuation
        })
        
        self.store_factors.store_profitability(ticker, effective_date, {
            **key_metrics,
            **financial_ratios,
            **growth_metrics.get("income", {})
        })
        
        self.store_factors.store_liquidity_solvent_efficiency(ticker, effective_date, {
            **key_metrics,
            **financial_ratios,
            **growth_metrics.get("balance", {})
        })
        
        # Store analyst ratings with proper mapping
        analyst_data = {
            "analystRatingsStrongBuy": company_info.get("strongBuy"),
            "analystRatingsBuy": company_info.get("buy"),
            "analystRatingsHold": company_info.get("hold"),
            "analystRatingsSell": company_info.get("sell"),
            "analystRatingsStrongSell": company_info.get("strongSell"),
            "all_time_avg_price_target": company_info.get("allTimeAvgPriceTarget"),
            "last_month_avg_price_target": company_info.get("lastMonthAvgPriceTarget"),
            "last_quarter_avg_price_target": company_info.get("lastQuarterAvgPriceTarget"),
            "last_year_avg_price_target": company_info.get("lastYearAvgPriceTarget"),
            "consensus": company_info.get("consensus"),
            "target_high": company_info.get("targetHigh"),
            "target_low": company_info.get("targetLow"),
            "target_median": company_info.get("targetMedian"),
            "numAnalystsEps": company_info.get("numAnalystsEps"),
            "numAnalystsRevenue": company_info.get("numAnalystsRevenue")
        }
        self.store_factors.store_analyst_ratings(ticker, effective_date, analyst_data)
        
        # Store technical indicators with proper mapping
        technical_data = {
            "beta": company_info.get("beta"),
            "averageChange": company_info.get("changes"),
            "stock_price": company_info.get("price"),
            "stockPrice": company_info.get("price"),
            "price_range": company_info.get("price_range"),
            "rating": company_info.get("rating"),
            "overallScore": company_info.get("overallScore"),
            "discountedCashFlowScore": company_info.get("dcfScore"),
            "priceToBookScore": company_info.get("priceToBookScore"),
            "priceToEarningsScore": company_info.get("priceToEarningsScore"),
            "returnOnAssetsScore": company_info.get("returnOnAssetsScore"),
            "returnOnEquityScore": company_info.get("returnOnEquityScore")
        }
        self.store_factors.store_technical_indicators(ticker, effective_date, technical_data)
        
        # Store price data
        price_data = data.get("price_data", {})
        if price_data:
            self.store_prices.store_daily_prices(ticker, price_data)
        
        # Store EPS and revenue estimates with proper mapping
        eps_data = {
            "epsEstimated": key_metrics.get("epsEstimated"),
            "epsActual": key_metrics.get("epsActual"),
            "epsAvg": key_metrics.get("epsAvg"),
            "epsHigh": key_metrics.get("epsHigh"),
            "epsLow": key_metrics.get("epsLow"),
            "revenueEstimated": key_metrics.get("revenueEstimated"),
            "revenueActual": key_metrics.get("revenueActual"),
            "revenueAvg": key_metrics.get("revenueAvg"),
            "revenueHigh": key_metrics.get("revenueHigh"),
            "revenueLow": key_metrics.get("revenueLow")
        }
        self.store_estimates.store_eps_revenue(ticker, effective_date, eps_data)

        # Store economic indicators
        economic_indicators = data.get("economic_indicators", {})
        if economic_indicators:
            for indicator_name, indicator_data in economic_indicators.items():
                if isinstance(indicator_data, list) and indicator_data:
                    latest_data = indicator_data[0]
                    value = latest_data.get("value")
                    indicator_date = latest_data.get("date")
                    if value is not None and indicator_date is not None:
                        if "rate" in indicator_name:
                            self.store_macro.store_rate(indicator_name, indicator_date, value)
                        else:
                            self.store_macro.store_economic_indicator(indicator_name, indicator_date, value) 