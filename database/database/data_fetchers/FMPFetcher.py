import time
from typing import List, Optional, Dict, Any
import sys
from pathlib import Path

# Add project root to Python path
project_root = str(Path(__file__).parent.parent.parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from database.endpoints.FMPEndpoint import FMPEndpoint
from database.database.config.data_fetch_config import DataFetchConfig

class FMPFetcher:
    def __init__(self, config: Optional[DataFetchConfig] = None):
        self.config = config or DataFetchConfig()
        self.fetcher = FMPEndpoint()
    
    def _with_retry(self, func, label: str):
        """Retry mechanism for API calls"""
        for attempt in range(self.config.max_retries):
            try:
                if attempt > 0:
                    print(f"Retry {attempt + 1} for {label}...")
                    time.sleep(self.config.retry_delay)
                return func()
            except Exception as e:
                print(f"Error on attempt {attempt + 1} for {label}: {e}")
                if attempt == self.config.max_retries - 1:
                    raise 

    #region Analyis
    def get_analyst_estimates(
        self,
        ticker: str,
        period: str,
        page: int,
        limit: int
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch raw analyst estimates from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_analyst_estimates(ticker, period, page, limit),
            f"analyst estimates for {ticker}"
        )

    def get_ratings(
        self,
        ticker: str,
        limit: int
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch raw ratings from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_ratings_historical(ticker, limit),
            f"ratings for {ticker}"
        )
    #endregion

    #region Analyst Data
    def get_price_target_summary(
        self,
        ticker: str
    ) -> Optional[Dict[str, Any]]:
        """Fetch price target summary from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_price_target_summary(ticker),
            f"price target summary for {ticker}"
        )

    def get_price_target_consensus(
        self,
        ticker: str
    ) -> Optional[Dict[str, Any]]:
        """Fetch price target consensus from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_price_target_consensus(ticker),
            f"price target consensus for {ticker}"
        )

    def get_grades_historical(
        self,
        ticker: str,
        limit: int
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch historical grades from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_grades_historical(ticker, limit),
            f"historical grades for {ticker}"
        )

    def get_grades_consensus(
        self,
        ticker: str
    ) -> Optional[Dict[str, Any]]:
        """Fetch grades consensus from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_grades_consensus(ticker),
            f"grades consensus for {ticker}"
            )
    #endregion

    #region Core
    def get_stocks(
        self,
        ticker: str
    ) -> Optional[Dict[str, Any]]:
        """Fetch stocks from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_company_screener(ticker),
            f"stocks for {ticker}"
        )

    def get_employee_count(
        self,
        ticker: str,
        limit: int
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch employee count from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_historical_employee_count(ticker, limit),
            f"employee count for {ticker}"
        )
    
    def get_historical_employee_count(
        self,
        ticker: str,
        limit: int
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch historical employee count from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_historical_employee_count(ticker, limit),
            f"employee count for {ticker}"
        )
    #endregion  

    #region Financial Metrics
    def get_key_metrics(
        self,
        ticker: str,
        limit: int,
        period: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch key metrics from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_key_metrics(ticker, limit, period),
            f"key metrics for {ticker}"
        )
    
    def get_earnings(
        self,
        ticker: str,
        limit: int
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch earnings from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_earnings(ticker, limit),
            f"earnings for {ticker}"
        )

    def get_financial_ratios(
        self,
        ticker: str,
        limit: int,
        period: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch financial ratios from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_financial_ratios(ticker, limit, period),
            f"financial ratios for {ticker}"
        )
    #endregion

    #region Growth
    def get_income_statement_growth(
        self,
        ticker: str,
        limit: int,
        period: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch income statement growth from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_income_statement_growth(ticker, limit, period),
            f"income statement growth for {ticker}"
        )

    def get_balance_sheet_growth(
        self,
        ticker: str,
        limit: int,
        period: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch balance sheet growth from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_balance_sheet_growth(ticker, limit, period),
            f"balance sheet growth for {ticker}"
        )

    def get_cashflow_statement_growth(
        self,
        ticker: str,
        limit: int,
        period: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch cashflow statement growth from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_cashflow_statement_growth(ticker, limit, period),
            f"cashflow statement growth for {ticker}"
        )

    def get_financial_statement_growth(
        self,
        ticker: str,
        limit: int,
        period: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch financial statement growth from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_financial_statement_growth(ticker, limit, period),
            f"financial statement growth for {ticker}"
        )
    #endregion

    #region Market Data
    def get_dividends(
        self,
        ticker: str,
        limit: int
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch dividends from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_dividends(ticker, limit),
            f"dividends for {ticker}"
        )
    
    def get_splits(
        self,
        ticker: str,
        limit: int
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch stock splits from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_splits(ticker, limit),
            f"splits for {ticker}"
        )

    def get_price_volume_data(
        self,
        ticker: str,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch price and volume data from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_price_volume_data(ticker, from_date, to_date),
            f"price volume data for {ticker}"
        )

    def get_dividend_adjusted_prices(
        self,
        ticker: str,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch dividend adjusted prices from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_dividend_adjusted_prices(ticker, from_date, to_date),
            f"dividend adjusted prices for {ticker}"
        )
    
    def get_historical_market_cap(
        self,
        ticker: str,
        limit: int,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch historical market cap from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_historical_market_cap(ticker, limit, from_date, to_date),
            f"market cap for {ticker}"
        )
    
    def get_share_float(
        self,
        ticker: str
    ) -> Optional[Dict[str, Any]]:
        """Fetch share float from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_share_float(ticker),
            f"share float for {ticker}"
        )
    #endregion

    #region Valuation
    def get_discounted_cash_flow(
        self,
        ticker: str
    ) -> Optional[Dict[str, Any]]:
        """Fetch discounted cash flow from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_discounted_cash_flow(ticker),
            f"discounted cash flow for {ticker}"
        )

    def get_levered_discounted_cash_flow(
        self,
        ticker: str
    ) -> Optional[Dict[str, Any]]:
        """Fetch levered discounted cash flow from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_levered_discounted_cash_flow(ticker),
            f"levered discounted cash flow for {ticker}"
        )
    
    def get_owner_earnings(
        self,
        ticker: str,
        limit: int
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch owner earnings from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_owner_earnings(ticker, limit),
            f"owner earnings for {ticker}"
        )

    def get_enterprise_values(
        self,
        ticker: str,
        limit: int,
        period: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch enterprise values from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_enterprise_values(ticker, limit, period),
            f"enterprise values for {ticker}"
        )
    #endregion

    #region Macro
    def get_latest_mergers_acquisitions(
        self,
        page: int,
        limit: int
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch latest mergers and acquisitions from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_latest_mergers_acquisitions(page, limit),
            "latest mergers and acquisitions"
        )

    def get_treasury_rates(
        self,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch treasury rates from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_treasury_rates(from_date, to_date),
            "treasury rates"
        )

    def get_historical_sector_performance(
        self,
        sector: str,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        exchange: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch historical sector performance from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_historical_sector_performance(sector, from_date, to_date, exchange),
            f"sector performance for {sector}"
        )

    def get_historical_industry_performance(
        self,
        industry: str,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        exchange: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch historical industry performance from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_historical_industry_performance(industry, from_date, to_date, exchange),
            f"industry performance for {industry}"
        )

    def get_historical_sector_pe(
        self,
        sector: str,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        exchange: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch historical sector P/E from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_historical_sector_pe(sector, from_date, to_date, exchange),
            f"sector P/E for {sector}"
        )

    def get_historical_industry_pe(
        self,
        industry: str,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        exchange: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch historical industry P/E from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_historical_industry_pe(industry, from_date, to_date, exchange),
            f"industry P/E for {industry}"
        )

    def get_economic_indicators(
        self,
        name: str,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetch economic indicator from FMP API"""
        return self._with_retry(
            lambda: self.fetcher.get_economic_indicators(name, from_date, to_date),
            f"economic indicators {name}"
        )
    #endregion
