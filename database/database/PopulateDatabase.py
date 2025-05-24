from datetime import datetime, timedelta
import logging
from typing import Dict, Any, Optional, List
from .StockDatabase import StockDatabase
from .db_writers import *
from .db_writers.DataFetcher import DataFetcher

class PopulateDatabase:
    def __init__(self, db: StockDatabase):
        self.db = db
        self.data_fetcher = DataFetcher()
        conn = self.db._get_connection()
        
        self.store_core = StoreCore(conn)
        self.store_market_data = StoreMarketData(conn)
        self.store_valuation = StoreValuation(conn)
        self.store_financial_metrics = StoreFinancialMetrics(conn)
        self.store_growth = StoreGrowth(conn)
        self.store_analysis = StoreAnalysis(conn)
        self.store_corporate_actions = StoreCorporateActions(conn)
        self.store_analysis_data = StoreAnalysisData(conn)
        self.store_macro = StoreMacro(conn)
        self.store_analysis = StoreAnalysis(conn)

        logging.basicConfig(level=logging.INFO)

    def populate(self, tickers: Optional[List[str]] = None):
        if tickers is None:
            tickers = self.data_fetcher.get_sp500_tickers()
            logging.info(f"Using default tickers from S&P 500 ({len(tickers)} tickers)")
        else:
            logging.info(f"Populating data for provided tickers: {tickers}")

        self.populate_batch(tickers)

    def populate_batch(self, tickers: List[str]):
        for ticker in tickers:
            logging.info(f"Starting population for ticker: {ticker}")
            self.populate_one_ticker(ticker)

    def populate_one_ticker(self, ticker: str):
        try:
            # Fetch all data for the ticker
            data = self._fetch_all_data(ticker)
            date = datetime.now().strftime('%Y-%m-%d')

            self._store_core_data(ticker, data)
            self._store_market_data(ticker, data)
            self._store_financial_metrics(ticker, date, data)
            self._store_valuation_data(ticker, date, data)
            self._store_analyst_data(ticker, date, data)
            self._store_corporate_actions(ticker, data)
            self._store_macro_data(ticker, date, data)
            
            logging.info(f"Successfully populated data for ticker: {ticker}")
        except Exception as e:
            logging.error(f"Failed to populate {ticker}: {e}")

    def _fetch_all_data(self, ticker: str) -> Dict[str, Any]:
        # Fetch company info and basic data
        company_info = self.data_fetcher.fetcher.get_exchange_variant(ticker)
        
        # Fetch market data
        price_data = self.data_fetcher.download_with_retry([ticker],
                                              (datetime.now() - timedelta(days=365)),
                                              datetime.now())
        
        # Fetch financial data
        key_metrics = self.data_fetcher.fetcher.get_key_metrics(ticker, limit=1)
        financial_ratios = self.data_fetcher.fetcher.get_financial_ratios(ticker, limit=1)
        
        # Fetch valuation data
        dcf = self.data_fetcher.fetcher.get_discounted_cash_flow(ticker)
        levered_dcf = self.data_fetcher.fetcher.get_levered_discounted_cash_flow(ticker)
        enterprise_values = self.data_fetcher.fetcher.get_enterprise_values(ticker, limit=1)
        owner_earnings = self.data_fetcher.fetcher.get_owner_earnings(ticker, limit=1)
        
        # Fetch analyst data
        analyst_estimates = self.data_fetcher.fetcher.get_analyst_estimates(ticker)
        ratings = self.data_fetcher.fetcher.get_ratings_historical(ticker, limit=1)
        price_targets = self.data_fetcher.fetcher.get_price_target_summary(ticker)
        price_target_consensus = self.data_fetcher.fetcher.get_price_target_consensus(ticker)
        grades = self.data_fetcher.fetcher.get_grades_historical(ticker, limit=1)
        grades_consensus = self.data_fetcher.fetcher.get_grades_consensus(ticker)
        
        # Fetch corporate actions
        dividends = self.data_fetcher.fetcher.get_dividends(ticker)
        splits = self.data_fetcher.fetcher.get_splits(ticker)
        earnings = self.data_fetcher.fetcher.get_earnings(ticker)
        mergers = self.data_fetcher.fetcher.get_latest_mergers_acquisitions()
        
        # Fetch additional market data
        market_cap = self.data_fetcher.fetcher.get_historical_market_cap(ticker, limit=1)
        share_float = self.data_fetcher.fetcher.get_share_float(ticker)
        employee_count = self.data_fetcher.fetcher.get_historical_employee_count(ticker, limit=1)
        
        # Fetch macro data
        economic_indicators = self.data_fetcher.fetcher.get_selected_economic_indicators()
        
        return {
            "company_info": company_info,
            "price_data": price_data,
            "key_metrics": key_metrics[0] if key_metrics else {},
            "financial_ratios": financial_ratios[0] if financial_ratios else {},
            "valuation": {
                "dcf": dcf,
                "levered_dcf": levered_dcf,
                "enterprise_values": enterprise_values[0] if enterprise_values else {},
                "owner_earnings": owner_earnings[0] if owner_earnings else {}
            },
            "analyst_data": {
                "estimates": analyst_estimates,
                "ratings": ratings[0] if ratings else {},
                "price_targets": price_targets,
                "price_target_consensus": price_target_consensus,
                "grades": grades[0] if grades else {},
                "grades_consensus": grades_consensus
            },
            "corporate_actions": {
                "dividends": dividends,
                "splits": splits,
                "earnings": earnings,
                "mergers": mergers
            },
            "market_data": {
                "market_cap": market_cap[0] if market_cap else {},
                "share_float": share_float,
                "employee_count": employee_count[0] if employee_count else {}
            },
            "economic_indicators": economic_indicators
        }

    def _store_core_data(self, ticker: str, data: Dict[str, Any]):
        company_info = data.get("company_info", {})
        if company_info:
            self.store_factors.store_stock_info(ticker, company_info)
        
        employee_count = data.get("market_data", {}).get("employee_count", {})
        if employee_count:
            self.store_factors.store_employee_count(ticker, employee_count)

    def _store_market_data(self, ticker: str, data: Dict[str, Any]):
        # Store price data
        price_data = data.get("price_data", {})
        if price_data is not None and ticker in price_data.columns:
            price_dict = {date.strftime('%Y-%m-%d'): float(value) 
                         for date, value in price_data[ticker].dropna().items()}
            self.store_prices.store_daily_prices(ticker, price_dict)
        
        # Store market cap
        market_cap = data.get("market_data", {}).get("market_cap", {})
        if market_cap:
            self.store_prices.store_market_cap(ticker, market_cap)
        
        # Store share float
        share_float = data.get("market_data", {}).get("share_float", {})
        if share_float:
            self.store_prices.store_share_float(ticker, share_float)

    def _store_financial_metrics(self, ticker: str, date: str, data: Dict[str, Any]):
        # Store key metrics
        key_metrics = data.get("key_metrics", {})
        if key_metrics:
            self.store_factors.store_key_metrics(ticker, date, key_metrics)
        
        # Store financial ratios
        financial_ratios = data.get("financial_ratios", {})
        if financial_ratios:
            self.store_factors.store_financial_ratios(ticker, date, financial_ratios)

    def _store_valuation_data(self, ticker: str, date: str, data: Dict[str, Any]):
        valuation = data.get("valuation", {})
        if valuation:
            if "dcf" in valuation:
                self.store_factors.store_dcf(ticker, date, valuation["dcf"])
            if "levered_dcf" in valuation:
                self.store_factors.store_levered_dcf(ticker, date, valuation["levered_dcf"])
            if "enterprise_values" in valuation:
                self.store_factors.store_enterprise_values(ticker, date, valuation["enterprise_values"])
            if "owner_earnings" in valuation:
                self.store_factors.store_owner_earnings(ticker, date, valuation["owner_earnings"])

    def _store_analyst_data(self, ticker: str, date: str, data: Dict[str, Any]):
        analyst_data = data.get("analyst_data", {})
        if analyst_data:
            if "estimates" in analyst_data:
                self.store_estimates.store_eps_revenue(ticker, date, analyst_data["estimates"])
            if "ratings" in analyst_data:
                self.store_factors.store_analyst_ratings(ticker, date, analyst_data["ratings"])
            if "price_targets" in analyst_data:
                self.store_factors.store_price_target_summary(ticker, date, analyst_data["price_targets"])
            if "price_target_consensus" in analyst_data:
                self.store_factors.store_price_target_consensus(ticker, date, analyst_data["price_target_consensus"])
            if "grades" in analyst_data:
                self.store_factors.store_grades(ticker, date, analyst_data["grades"])
            if "grades_consensus" in analyst_data:
                self.store_factors.store_grades_consensus(ticker, date, analyst_data["grades_consensus"])

    def _store_corporate_actions(self, ticker: str, data: Dict[str, Any]):
        corporate_actions = data.get("corporate_actions", {})
        if corporate_actions:
            if "dividends" in corporate_actions:
                self.store_factors.store_dividends(ticker, corporate_actions["dividends"])
            if "splits" in corporate_actions:
                self.store_factors.store_splits(ticker, corporate_actions["splits"])
            if "earnings" in corporate_actions:
                self.store_factors.store_earnings(ticker, corporate_actions["earnings"])
            if "mergers" in corporate_actions:
                self.store_factors.store_mergers_acquisitions(ticker, corporate_actions["mergers"])

    def _store_macro_data(self, ticker: str, date: str, data: Dict[str, Any]):
        economic_indicators = data.get("economic_indicators", {})
        if economic_indicators:
            for indicator_name, indicator_data in economic_indicators.items():
                if isinstance(indicator_data, dict) and "value" in indicator_data and "date" in indicator_data:
                    if "rate" in indicator_name:
                        self.store_macro.store_rate(indicator_name, indicator_data["date"], indicator_data["value"])
                    else:
                        self.store_macro.store_economic_indicator(indicator_name, indicator_data["date"], indicator_data["value"])
