import os
import requests
import time
import logging
from typing import Any, Dict, List, Optional, Union
from requests.exceptions import RequestException
from dotenv import load_dotenv
from datetime import datetime
from .base import FinancialDataEndpoint

# Configure logging
logging.basicConfig(level=logging.INFO)
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
    
    #region Core
    def get_company_screener(self, symbol: str) -> dict:
        """Fetch filtered exchange variant data for a symbol."""
        url = f"{BASE_URL}/company-screener"
        data = self.get_json(url)
        if not data or not isinstance(data, list):
            return {}

        for entry in data:
            if entry.get("symbol", "").upper() == symbol.upper():
                return {
                    "symbol": entry.get("symbol"),
                    "company_name": entry.get("companyName"),
                    "exchange_short_name": entry.get("exchangeShortName"),
                    "industry": entry.get("industry"),
                    "sector": entry.get("sector"),
                    "country": entry.get("country"),
                    "is_actively_trading": entry.get("isActivelyTrading"),
                }

    def get_historical_employee_count(self, symbol: str, limit: int = None) -> list[dict]:
        """Fetch historical employee count data for a company."""
        url = f"{BASE_URL}/employee-count"
        params = {
            "symbol": symbol
        }
        if limit is not None:
            params["limit"] = limit

        data = self.get_json(url, params=params)
        if not isinstance(data, list):
            return []
        
        return [{
            "symbol": entry.get("symbol"),
            "date": entry.get("filingDate"),
            "employeeCount": entry.get("employeeCount")
        } for entry in data]
    #endregion

    #region Analysis
    def get_analyst_estimates(self, symbol: str, period: str = "annual", page: int = 0, limit: int = 10) -> list[dict]:
        """Fetch full analyst estimates data for a symbol."""
        url = f"{BASE_URL}/analyst-estimates"
        params = {
            "symbol": symbol,
            "period": period,
            "page": page,
            "limit": limit
        }
        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []
        
    def get_ratings_historical(self, symbol: str, limit: int = None) -> list[dict]:
        """Fetch historical ratings data for a symbol."""
        url = f"{BASE_URL}/ratings-historical"
        params = {
            "symbol": symbol
        }
        if limit is not None:
            params["limit"] = limit

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []
    #endregion

    #region Analyst Data
    def get_price_target_summary(self, symbol: str) -> dict:
        """Fetch summarized price target data for a symbol, excluding publishers."""
        url = f"{BASE_URL}/price-target-summary"
        params = {
            "symbol": symbol
        }

        data = self.get_json(url, params=params)
        if not data or not isinstance(data, list):
            return {}

        entry = data[0]
        return {
            "symbol": entry.get("symbol"),
            "last_month_count": entry.get("lastMonthCount"),
            "last_month_avg_price_target": entry.get("lastMonthAvgPriceTarget"),
            "last_quarter_count": entry.get("lastQuarterCount"),
            "last_quarter_avg_price_target": entry.get("lastQuarterAvgPriceTarget"),
            "last_year_count": entry.get("lastYearCount"),
            "last_year_avg_price_target": entry.get("lastYearAvgPriceTarget"),
            "all_time_count": entry.get("allTimeCount"),
            "all_time_avg_price_target": entry.get("allTimeAvgPriceTarget")
        }

    def get_price_target_consensus(self, symbol: str) -> dict:
        """Fetch price target consensus data for a symbol."""
        url = f"{BASE_URL}/price-target-consensus"
        params = {
            "symbol": symbol
        }

        data = self.get_json(url, params=params)
        if not data or not isinstance(data, list):
            return {}

        entry = data[0]
        return {
            "symbol": entry.get("symbol"),
            "target_high": entry.get("targetHigh"),
            "target_low": entry.get("targetLow"),
            "target_consensus": entry.get("targetConsensus"),
            "target_median": entry.get("targetMedian")
        }
        
    def get_grades_historical(self, symbol: str, limit: int = None) -> list[dict]:
        """Fetch historical analyst grades for a symbol."""
        url = f"{BASE_URL}/grades-historical"
        params = {
            "symbol": symbol
        }
        if limit is not None:
            params["limit"] = limit

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []
    
    def get_grades_consensus(self, symbol: str) -> dict:
        """Fetch analyst consensus grades for a symbol."""
        url = f"{BASE_URL}/grades-consensus"
        params = {
            "symbol": symbol
        }

        data = self.get_json(url, params=params)
        if not data or not isinstance(data, list):
            return {}

        entry = data[0]
        return {
            "symbol": entry.get("symbol"),
            "strong_buy": entry.get("strongBuy"),
            "buy": entry.get("buy"),
            "hold": entry.get("hold"),
            "sell": entry.get("sell"),
            "strong_sell": entry.get("strongSell"),
            "consensus": entry.get("consensus")
        }
    #endregion

    #region Financial Metrics
    def get_key_metrics(
        self, symbol: str, limit: int = None, period: str = None
    ) -> list[dict]:
        """Fetch financial key metrics for a company."""
        url = f"{BASE_URL}/key-metrics"
        params = {
            "symbol": symbol
        }
        if limit is not None:
            params["limit"] = limit
        if period is not None:
            params["period"] = period

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []
        
    def get_financial_ratios(
        self, symbol: str, limit: int = None, period: str = None
    ) -> list[dict]:
        """Fetch financial ratios for a company."""
        url = f"{BASE_URL}/ratios"
        params = {
            "symbol": symbol
        }
        if limit is not None:
            params["limit"] = limit
        if period is not None:
            params["period"] = period

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []

    def get_earnings(self, symbol: str, limit: int = None) -> list[dict]:
        """Fetch earnings history for a symbol."""
        url = f"{BASE_URL}/earnings"
        params = {
            "symbol": symbol
        }
        if limit is not None:
            params["limit"] = limit

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []
    #endregion

    #region Growth
    def get_income_statement_growth(
        self, symbol: str, limit: int = None, period: str = None
    ) -> list[dict]:
        """Fetch income statement growth metrics for a company."""
        url = f"{BASE_URL}/income-statement-growth"
        params = {
            "symbol": symbol
        }
        if limit is not None:
            params["limit"] = limit
        if period is not None:
            params["period"] = period

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []
        
    def get_balance_sheet_growth(
        self, symbol: str, limit: int = None, period: str = None
    ) -> list[dict]:
        """Fetch balance sheet growth metrics for a company."""
        url = f"{BASE_URL}/balance-sheet-statement-growth"
        params = {
            "symbol": symbol
        }
        if limit is not None:
            params["limit"] = limit
        if period is not None:
            params["period"] = period

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []
        
    def get_cashflow_statement_growth(
        self, symbol: str, limit: int = None, period: str = None
    ) -> list[dict]:
        """Fetch cashflow statement growth metrics for a company."""
        url = f"{BASE_URL}/cash-flow-statement-growth"
        params = {
            "symbol": symbol
        }
        if limit is not None:
            params["limit"] = limit
        if period is not None:
            params["period"] = period

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []
    
    def get_financial_statement_growth(
        self, symbol: str, limit: int = None, period: str = None
    ) -> list[dict]:
        """Fetch overall financial statement growth metrics for a company."""
        url = f"{BASE_URL}/financial-growth"
        params = {
            "symbol": symbol
        }
        if limit is not None:
            params["limit"] = limit
        if period is not None:
            params["period"] = period

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []
    #endregion
    
    #region Market Data
    def get_dividends(self, symbol: str, limit: int = None) -> list[dict]:
        """Fetch dividend history for a symbol, excluding recordDate and paymentDate."""
        url = f"{BASE_URL}/dividends"
        params = {
            "symbol": symbol
        }
        if limit is not None:
            params["limit"] = limit

        data = self.get_json(url, params=params)
        if not isinstance(data, list):
            return []

        return [
            {
                "symbol": entry.get("symbol"),
                "date": entry.get("date"),
                "declaration_date": entry.get("declarationDate"),
                "adj_dividend": entry.get("adjDividend"),
                "dividend": entry.get("dividend"),
                "yield": entry.get("yield"),
                "frequency": entry.get("frequency")
            }
            for entry in data
        ]
    
    def get_dividend_adjusted_prices(
        self, symbol: str, from_date: str = None, to_date: str = None
    ) -> list[dict]:
        """Fetch dividend-adjusted historical price and volume data for a symbol."""
        url = f"{BASE_URL}/historical-price-eod/dividend-adjusted"
        params = {
            "symbol": symbol
        }
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        data = self.get_json(url, params=params)
        if not isinstance(data, list):
            return []
            
        # Map the API response fields to our expected format
        return [{
            "symbol": entry.get("symbol"),
            "date": entry.get("date"),
            "open": entry.get("open"),
            "high": entry.get("high"),
            "low": entry.get("low"),
            "close": entry.get("close"),
            "adjOpen": entry.get("adjOpen"),
            "adjHigh": entry.get("adjHigh"),
            "adjLow": entry.get("adjLow"),
            "adjClose": entry.get("adjClose"),
            "volume": entry.get("volume"),
            "unadjustedVolume": entry.get("unadjustedVolume"),
            "change": entry.get("change"),
            "changePercent": entry.get("changePercent"),
            "vwap": entry.get("vwap"),
            "label": entry.get("label"),
            "changeOverTime": entry.get("changeOverTime")
        } for entry in data]

    def get_historical_market_cap(
        self, symbol: str, limit: int = None, from_date: str = None, to_date: str = None
    ) -> list[dict]:
        """Fetch historical market capitalization data for a company."""
        url = f"{BASE_URL}/historical-market-capitalization"
        params = {
            "symbol": symbol
        }
        if limit is not None:
            params["limit"] = limit
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []
    
    def get_share_float(self, symbol: str) -> dict:
        """Fetch company share float and liquidity data."""
        url = f"{BASE_URL}/shares-float"
        params = {
            "symbol": symbol
        }

        data = self.get_json(url, params=params)
        if not data or not isinstance(data, list):
            return {}
        entry = data[0]
        return {
            "symbol": entry.get("symbol"),
            "date": entry.get("date"),
            "free_float": entry.get("freeFloat"),
            "float_shares": entry.get("floatShares"),
            "outstanding_shares": entry.get("outstandingShares")
        }
    
    def get_splits(self, symbol: str, limit: int = None) -> list[dict]:
        """Fetch stock split history for a symbol."""
        url = f"{BASE_URL}/splits"
        params = {
            "symbol": symbol
        }
        if limit is not None:
            params["limit"] = limit

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []
    
    def get_price_volume_data(
        self, symbol: str, from_date: str = None, to_date: str = None
    ) -> list[dict]:
        """Fetch full historical price and volume data for a symbol."""
        url = f"{BASE_URL}/historical-price-eod/full"
        params = {
            "symbol": symbol
        }
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []
    #endregion
    
    #region Macro
    def get_latest_mergers_acquisitions(self, page: int = 0, limit: int = 100) -> list[dict]:
        """Fetch the latest mergers and acquisitions data."""
        url = f"{BASE_URL}/mergers-acquisitions-latest"
        params = {
            "page": page,
            "limit": limit
        }

        data = self.get_json(url, params=params)
        if not isinstance(data, list):
            return []
        
        return [{
            "symbol": entry.get("symbol"),
            "targetedSymbol": entry.get("targetedSymbol"),
            "transactionDate": entry.get("transactionDate"),
            "transactionDate": entry.get("transactionDate"),
        } for entry in data]
    
    def get_historical_sector_performance(
        self, sector: str, from_date: str = None, to_date: str = None, exchange: str = None
    ) -> list[dict]:
        """Fetch historical sector performance data."""
        url = f"{BASE_URL}/historical-sector-performance"
        params = {
            "sector": sector
        }
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date
        if exchange:
            params["exchange"] = exchange

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []

    def get_historical_industry_performance(
        self, industry: str, from_date: str = None, to_date: str = None, exchange: str = None
    ) -> list[dict]:
        """Fetch historical performance data for a given industry."""
        url = f"{BASE_URL}/historical-industry-performance"
        params = {
            "industry": industry
        }
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date
        if exchange:
            params["exchange"] = exchange

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []
    
    def get_historical_sector_pe(
        self, sector: str, from_date: str = None, to_date: str = None, exchange: str = None
    ) -> list[dict]:
        """Fetch historical P/E ratios for a given sector."""
        url = f"{BASE_URL}/historical-sector-pe"
        params = {
            "sector": sector
        }
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date
        if exchange:
            params["exchange"] = exchange

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []
    
    def get_historical_industry_pe(
        self, industry: str, from_date: str = None, to_date: str = None, exchange: str = None
    ) -> list[dict]:
        """Fetch historical P/E ratios for a given industry."""
        url = f"{BASE_URL}/historical-industry-pe"
        params = {
            "industry": industry
        }
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date
        if exchange:
            params["exchange"] = exchange

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []

    def get_selected_economic_indicators(self, from_date: str = None, to_date: str = None) -> dict:
        """Fetch selected economic indicators."""
        indicator_names = [
            "GDP",
            "realGDP",
            "federalFunds",
            "CPI",
            "inflationRate",
            "retailSales",
            "consumerSentiment",
            "durableGoods",
            "unemploymentRate",
            "totalNonfarmPayroll",
            "industrialProductionTotalIndex",
            "totalVehicleSales",
            "3MonthOr90DayRatesAndYieldsCertificatesOfDeposit",
            "30YearFixedRateMortgageAverage"
        ]

        results = {}
        for name in indicator_names:
            key = name.lower().replace(" ", "_")
            results[key] = self.get_economic_indicator(name, from_date, to_date)

        return results
    
    def get_economic_indicator(self, name: str = "GDP", from_date: str = None, to_date: str = None) -> list[dict]:
        """Fetch economic indicator data by name.
        
        Args:
            name: The name of the economic indicator. Defaults to "GDP" if not provided.
            from_date: Optional start date for the data range
            to_date: Optional end date for the data range
            
        Returns:
            List of dictionaries containing the economic indicator data
        """
        url = f"{BASE_URL}/economic-indicators?name={name}"
        params = {}
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []
    
    def get_treasury_rates(self, from_date: str = None, to_date: str = None) -> list[dict]:
        """Fetch real-time and historical Treasury rates across all maturities."""
        url = f"{BASE_URL}/treasury-rates"
        params = {}
        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []
    #endregion

    #region Valuation
    def get_discounted_cash_flow(self, symbol: str) -> dict:
        """Fetch standard Discounted Cash Flow (DCF) valuation for a symbol."""
        url = f"{BASE_URL}/discounted-cash-flow"
        params = {
            "symbol": symbol
        }

        data = self.get_json(url, params=params)
        if not data or not isinstance(data, list):
            return {}
        entry = data[0]
        return {
            "symbol": entry.get("symbol"),
            "date": entry.get("date"),
            "dcf": entry.get("dcf"),
            "stock_price": entry.get("Stock Price")
        }

    def get_levered_discounted_cash_flow(self, symbol: str) -> dict:
        """Fetch Levered Discounted Cash Flow (DCF) valuation for a symbol."""
        url = f"{BASE_URL}/levered-discounted-cash-flow"
        params = {
            "symbol": symbol
        }

        data = self.get_json(url, params=params)
        if not data or not isinstance(data, list):
            return {}
        entry = data[0]
        return {
            "symbol": entry.get("symbol"),
            "date": entry.get("date"),
            "dcf": entry.get("dcf"),
            "stock_price": entry.get("Stock Price")
        }
        
    def get_owner_earnings(self, symbol: str, limit: int = None) -> list[dict]:
        """Fetch owner earnings data for a company."""
        url = f"{BASE_URL}/owner-earnings"
        params = {
            "symbol": symbol
        }
        if limit is not None:
            params["limit"] = limit

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []
    
    def get_enterprise_values(
        self, symbol: str, limit: int = None, period: str = None
    ) -> list[dict]:
        """Fetch enterprise value data for a company."""
        url = f"{BASE_URL}/enterprise-values"
        params = {
            "symbol": symbol
        }
        if limit is not None:
            params["limit"] = limit
        if period is not None:
            params["period"] = period

        data = self.get_json(url, params=params)
        return data if isinstance(data, list) else []
    #endregion
