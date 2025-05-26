import os
import requests
import time
import logging
from typing import Any, Dict, List, Optional, Union
from requests.exceptions import RequestException
from dotenv import load_dotenv
from datetime import datetime
from .base import FinancialDataEndpoint
from .FMPConstants import EXCHANGES, SECTORS, INDUSTRIES, ECONOMIC_INDICATORS

# Configure logging to write to a file
log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'logs')
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, 'fmp_endpoint.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()
API_KEY = os.getenv("FMP_API_KEY")
BASE_URL = "https://financialmodelingprep.com/stable"
MAX_RETRIES = 3
RETRY_DELAY = 1
RATE_LIMIT_DELAY = 0.1  # 100ms

class FMPEndpoint(FinancialDataEndpoint):
    def __init__(self):
        """Initialize the FMP endpoint with API key validation."""
        if not API_KEY:
            raise ValueError("FMP_API_KEY environment variable is not set")
        self.last_request_time = 0
    
    def _rate_limit(self):
        """Implement rate limiting to avoid API throttling."""
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        if time_since_last_request < RATE_LIMIT_DELAY:
            time.sleep(RATE_LIMIT_DELAY - time_since_last_request)
        self.last_request_time = time.time()

    def get_json(self, url: str, params: dict = None, retries: int = MAX_RETRIES) -> Any:
        """Make an HTTP GET request and return the JSON response.
        
        Args:
            url: The URL to make the request to.
            params: Dictionary of URL parameters to include in the request.
            retries: Number of retry attempts if the request fails.
            
        Returns:
            The JSON response data.
            
        Raises:
            ValueError: If the API key is invalid.
        """
        self._rate_limit()
        if params is None:
            params = {}
        params["apikey"] = API_KEY

        for attempt in range(retries):
            try:
                response = requests.get(url, params=params)
                if response.status_code == 401:
                    raise ValueError("Invalid API key. Please check your FMP_API_KEY environment variable.")
                response.raise_for_status()
                data = response.json()
                if not data:
                    logger.warning(f"Empty response from {url}")
                    return None
                return data
            except (RequestException, ValueError) as e:
                if attempt == retries - 1:
                    logger.error(f"Failed to fetch data from {url} after {retries} attempts: {str(e)}")
                    return None
                time.sleep(RETRY_DELAY * (attempt + 1))

    def fetch(self, ticker: str) -> Dict[str, Any]:
        """Fetch a complete set of fundamental data for a single ticker.
        
        This method aggregates data from multiple endpoints to provide a comprehensive
        view of a company's financial data.
        
        Args:
            ticker: The stock ticker symbol to fetch data for.
            
        Returns:
            A dictionary containing the fundamental data for the ticker.
        """
        try:
            company_info = self.get_exchange_variant(ticker)
            key_metrics = self.get_key_metrics(ticker, limit=1)
            financial_ratios = self.get_financial_ratios(ticker, limit=1)
            income_growth = self.get_income_statement_growth(ticker, limit=1)
            balance_growth = self.get_balance_sheet_growth(ticker, limit=1)
            cashflow_growth = self.get_cashflow_statement_growth(ticker, limit=1)
            dcf = self.get_discounted_cash_flow(ticker)
            levered_dcf = self.get_levered_discounted_cash_flow(ticker)

            return {
                "company_info": company_info,
                "key_metrics": key_metrics[0] if key_metrics else {},
                "financial_ratios": financial_ratios[0] if financial_ratios else {},
                "growth_metrics": {
                    "income": income_growth[0] if income_growth else {},
                    "balance": balance_growth[0] if balance_growth else {},
                    "cashflow": cashflow_growth[0] if cashflow_growth else {}
                },
                "valuation": {
                    "dcf": dcf,
                    "levered_dcf": levered_dcf
                }
            }
        except Exception as e:
            logger.error(f"Error fetching data for {ticker}: {str(e)}")
            return {}

    def _process_response(self, data: Any) -> dict:
        if not data:
            return {}
        if isinstance(data, list):
            return data[0] if data and isinstance(data[0], dict) else {}
        if isinstance(data, dict):
            return data
        return {}
    
    def _fetch_list_data(
        self,
        endpoint: str,
        base_params: Dict[str, Any] = None,
        variants: Optional[List[str]] = None,
        variant_param: Optional[str] = None,
        other_params: Optional[Dict[str, Any]] = None
    ) -> List[dict]:
        """
        Generic handler for FMP list-returning endpoints with optional variant looping.

        - `endpoint`: The API endpoint (e.g., "historical-sector-pe")
        - `base_params`: Always-included parameters (e.g., {"from": ..., "to": ...})
        - `variants`: List of sectors, industries, etc.
        - `variant_param`: Key to loop on (e.g., "sector", "industry", "name")
        - `other_params`: Static query params applied to all requests
        """
        results = []
        base_params = base_params or {}
        other_params = other_params or {}

        if variants:
            for v in variants:
                params = {**base_params, **other_params, variant_param: v}
                url = f"{BASE_URL}/{endpoint}"
                data = self.get_json(url, params=params)
                if isinstance(data, list):
                    results.extend(data)
        else:
            params = {**base_params, **other_params}
            url = f"{BASE_URL}/{endpoint}"
            data = self.get_json(url, params=params)
            if isinstance(data, list):
                results.extend(data)

        return results

    def _fetch_symbol_data(
        self,
        endpoint: str,
        symbol: str,
        extra_params: Optional[Dict[str, Any]] = None
    ) -> List[dict]:
        params = {"symbol": symbol}
        if extra_params:
            params.update(extra_params)

        url = f"{BASE_URL}/{endpoint}"
        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []

    #region Core
    def get_company_screener(self, symbol: str) -> dict:
        """Fetch filtered exchange variant data for a symbol from screener list."""
        url = f"{BASE_URL}/company-screener"
        data = self.get_json(url)
        if not isinstance(data, list):
            return {}
        
        return next((entry for entry in data if entry.get("symbol", "").upper() == symbol.upper()), {})


    def get_historical_employee_count(self, symbol: str, limit: int = None) -> list[dict]:
        return self._fetch_symbol_data(
            "employee-count",
            symbol,
            {"limit": limit} if limit is not None else None
        )

    #endregion

    #region Analysis
    def get_analyst_estimates(
        self, symbol: str, period: str = "annual", page: int = 0, limit: int = 10
    ) -> list[dict]:
        return self._fetch_symbol_data(
            "analyst-estimates",
            symbol,
            {
                "period": period,
                "page": page,
                "limit": limit
            }
        )

    def get_ratings_historical(self, symbol: str, limit: int = None) -> list[dict]:
        return self._fetch_symbol_data(
            "ratings-historical",
            symbol,
            {"limit": limit} if limit is not None else None
        )
    #endregion

    #region Analyst Data
    def get_price_target_summary(self, symbol: str) -> list[dict]:
        return self._fetch_symbol_data("price-target-summary", symbol)

    def get_price_target_consensus(self, symbol: str) -> list[dict]:
        return self._fetch_symbol_data("price-target-consensus", symbol)

    def get_grades_historical(self, symbol: str, limit: int = None) -> list[dict]:
        return self._fetch_symbol_data(
            "grades-historical",
            symbol,
            {"limit": limit} if limit is not None else None
        )

    def get_grades_consensus(self, symbol: str) -> list[dict]:
        return self._fetch_symbol_data("grades-consensus", symbol)
    #endregion

    #region Financial Metrics
    def get_key_metrics(
        self, symbol: str, limit: int = None, period: str = None
    ) -> list[dict]:
        return self._fetch_symbol_data(
            "key-metrics",
            symbol,
            {k: v for k, v in {"limit": limit, "period": period}.items() if v is not None}
        )

    def get_financial_ratios(
        self, symbol: str, limit: int = None, period: str = None
    ) -> list[dict]:
        return self._fetch_symbol_data(
            "ratios",
            symbol,
            {k: v for k, v in {"limit": limit, "period": period}.items() if v is not None}
        )

    def get_earnings(self, symbol: str, limit: int = None) -> list[dict]:
        return self._fetch_symbol_data(
            "earnings",
            symbol,
            {"limit": limit} if limit is not None else None
        )
    #endregion

    #region Growth
    def get_income_statement_growth(
        self, symbol: str, limit: int = None, period: str = None
    ) -> list[dict]:
        return self._fetch_symbol_data(
            "income-statement-growth",
            symbol,
            {k: v for k, v in {"limit": limit, "period": period}.items() if v is not None}
        )

    def get_balance_sheet_growth(
        self, symbol: str, limit: int = None, period: str = None
    ) -> list[dict]:
        return self._fetch_symbol_data(
            "balance-sheet-statement-growth",
            symbol,
            {k: v for k, v in {"limit": limit, "period": period}.items() if v is not None}
        )

    def get_cashflow_statement_growth(
        self, symbol: str, limit: int = None, period: str = None
    ) -> list[dict]:
        return self._fetch_symbol_data(
            "cash-flow-statement-growth",
            symbol,
            {k: v for k, v in {"limit": limit, "period": period}.items() if v is not None}
        )

    def get_financial_statement_growth(
        self, symbol: str, limit: int = None, period: str = None
    ) -> list[dict]:
        return self._fetch_symbol_data(
            "financial-growth",
            symbol,
            {k: v for k, v in {"limit": limit, "period": period}.items() if v is not None}
        )
    #endregion
    
    #region Market Data
    def get_dividends(self, symbol: str, limit: int = None) -> list[dict]:
        return self._fetch_symbol_data("dividends", symbol, {"limit": limit} if limit else None)

    def get_dividend_adjusted_prices(
        self, symbol: str, from_date: str = None, to_date: str = None
    ) -> list[dict]:
        extra = {}
        if from_date:
            extra["from"] = from_date
        if to_date:
            extra["to"] = to_date
        return self._fetch_symbol_data("historical-price-eod/dividend-adjusted", symbol, extra if extra else None)

    def get_historical_market_cap(
        self, symbol: str, limit: int = None, from_date: str = None, to_date: str = None
    ) -> list[dict]:
        extra = {}
        if limit is not None:
            extra["limit"] = limit
        if from_date:
            extra["from"] = from_date
        if to_date:
            extra["to"] = to_date
        return self._fetch_symbol_data("historical-market-capitalization", symbol, extra if extra else None)


    def get_share_float(self, symbol: str) -> list[dict]:
        return self._fetch_symbol_data("shares-float", symbol)

    def get_splits(self, symbol: str, limit: int = None) -> list[dict]:
        return self._fetch_symbol_data("splits", symbol, {"limit": limit} if limit else None)

    def get_price_volume_data(
        self, symbol: str, from_date: str = None, to_date: str = None
    ) -> list[dict]:
        extra = {}
        if from_date:
            extra["from"] = from_date
        if to_date:
            extra["to"] = to_date
        return self._fetch_symbol_data("historical-price-eod/full", symbol, extra if extra else None)
    #endregion
    
    #region Macro
    def get_latest_mergers_acquisitions(self, page: int = 0, limit: int = 100) -> list[dict]:
        return self._fetch_list_data(
            endpoint="mergers-acquisitions-latest",
            base_params={"page": page, "limit": limit}
        )

    def get_historical_sector_performance(
        self,
        sector: str = None,
        from_date: str = None,
        to_date: str = None,
        exchange: str = None
    ) -> list[dict]:
        return self._fetch_list_data(
            endpoint="historical-sector-performance",
            base_params={"from": from_date, "to": to_date} if from_date or to_date else {},
            variants=[sector] if sector else SECTORS,
            variant_param="sector",
            other_params={"exchange": exchange} if exchange else {}
        )

    def get_historical_industry_performance(
        self,
        industry: str = None,
        from_date: str = None,
        to_date: str = None,
        exchange: str = None
    ) -> list[dict]:
        return self._fetch_list_data(
            endpoint="historical-industry-performance",
            base_params={"from": from_date, "to": to_date} if from_date or to_date else {},
            variants=[industry] if industry else INDUSTRIES,
            variant_param="industry",
            other_params={"exchange": exchange} if exchange else {}
        )

    def get_historical_sector_pe(
        self, sector: str = None, from_date: str = None, to_date: str = None, exchange: str = None
    ) -> List[dict]:
        return self._fetch_list_data(
            endpoint="historical-sector-pe",
            base_params={"from": from_date, "to": to_date} if from_date or to_date else {},
            variants=[sector] if sector else SECTORS,
            variant_param="sector",
            other_params={"exchange": exchange} if exchange else {}
        )

    def get_historical_industry_pe(
        self,
        industry: str = None,
        from_date: str = None,
        to_date: str = None,
        exchange: str = None
    ) -> list[dict]:
        return self._fetch_list_data(
            endpoint="historical-industry-pe",
            base_params={"from": from_date, "to": to_date} if from_date or to_date else {},
            variants=[industry] if industry else INDUSTRIES,
            variant_param="industry",
            other_params={"exchange": exchange} if exchange else {}
        )

    def get_economic_indicators(
        self, name: Union[str, List[str]] = None, from_date: str = None, to_date: str = None
    ) -> List[dict]:
        name_list = [name] if isinstance(name, str) else (name or ECONOMIC_INDICATORS)
        return self._fetch_list_data(
            endpoint="economic-indicators",
            base_params={"from": from_date, "to": to_date} if from_date or to_date else {},
            variants=name_list,
            variant_param="name"
        )
    
    def get_treasury_rates(self, from_date: str = None, to_date: str = None) -> list[dict]:
        return self._fetch_list_data(
            endpoint="treasury-rates",
            base_params={"from": from_date, "to": to_date} if from_date or to_date else {}
        )

    #endregion

    #region Valuation
    def get_discounted_cash_flow(self, symbol: str) -> list[dict]:
        return self._fetch_symbol_data("discounted-cash-flow", symbol)

    def get_levered_discounted_cash_flow(self, symbol: str) -> list[dict]:
        return self._fetch_symbol_data("levered-discounted-cash-flow", symbol)

    def get_owner_earnings(self, symbol: str, limit: int = None) -> list[dict]:
        return self._fetch_symbol_data("owner-earnings", symbol, {"limit": limit} if limit else None)

    def get_enterprise_values(
        self, symbol: str, limit: int = None, period: str = None
    ) -> list[dict]:
        extra = {}
        if limit is not None:
            extra["limit"] = limit
        if period is not None:
            extra["period"] = period
        return self._fetch_symbol_data("enterprise-values", symbol, extra if extra else None)
    #endregion
