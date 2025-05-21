import requests
import pandas as pd
from datetime import datetime
from typing import Union, List, Dict, Any
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FMP_API_KEY")

if not API_KEY:
    raise ValueError("FMP_API_KEY not set. Add it to your .env file.")


BASE_URL = "https://financialmodelingprep.com/api/v3"

def fetch_historical_prices(tickers: Union[str, List[str]], start_date: str, end_date: str) -> pd.DataFrame:
    if isinstance(tickers, str):
        tickers = [tickers]
    
    data_frames = []
    for ticker in tickers:
        url = f"{BASE_URL}/historical-price-full/{ticker}"
        params = {
            "from": start_date,
            "to": end_date,
            "apikey": API_KEY
        }
        response = requests.get(url, params=params)
        json_data = response.json()
        if "historical" in json_data:
            df = pd.DataFrame(json_data["historical"])
            df["ticker"] = ticker
            data_frames.append(df[["date", "ticker", "adjClose"]])
    
    if not data_frames:
        return pd.DataFrame()
    
    result = pd.concat(data_frames)
    result["date"] = pd.to_datetime(result["date"])
    return result.pivot(index="date", columns="ticker", values="adjClose")


def fetch_fundamentals(ticker: str) -> Dict[str, Any]:
    # Fetch company profile
    profile_url = f"{BASE_URL}/profile/{ticker}"
    profile_params = {"apikey": API_KEY}
    profile_response = requests.get(profile_url, params=profile_params)
    profile_data = profile_response.json()
    
    if not profile_data or not isinstance(profile_data, list):
        return {}
    
    profile = profile_data[0]
    
    # Fetch financial ratios
    ratios_url = f"{BASE_URL}/ratios/{ticker}"
    ratios_params = {"apikey": API_KEY}
    ratios_response = requests.get(ratios_url, params=ratios_params)
    ratios_data = ratios_response.json()
    
    # Fetch income statement for growth metrics
    income_url = f"{BASE_URL}/income-statement/{ticker}"
    income_params = {"apikey": API_KEY, "limit": 2}  # Get last 2 years for growth calculation
    income_response = requests.get(income_url, params=income_params)
    income_data = income_response.json()
    
    # Fetch balance sheet for investment metrics
    balance_url = f"{BASE_URL}/balance-sheet-statement/{ticker}"
    balance_params = {"apikey": API_KEY, "limit": 2}
    balance_response = requests.get(balance_url, params=balance_params)
    balance_data = balance_response.json()
    
    # Calculate growth rates if we have enough data
    earnings_growth = None
    sales_growth = None
    cash_flow_growth = None
    asset_growth_rate = None
    
    if len(income_data) >= 2:
        current_earnings = income_data[0].get('netIncome', 0)
        prev_earnings = income_data[1].get('netIncome', 0)
        if prev_earnings != 0:
            earnings_growth = (current_earnings - prev_earnings) / abs(prev_earnings)
        
        current_sales = income_data[0].get('revenue', 0)
        prev_sales = income_data[1].get('revenue', 0)
        if prev_sales != 0:
            sales_growth = (current_sales - prev_sales) / abs(prev_sales)
    
    if len(balance_data) >= 2:
        current_assets = balance_data[0].get('totalAssets', 0)
        prev_assets = balance_data[1].get('totalAssets', 0)
        if prev_assets != 0:
            asset_growth_rate = (current_assets - prev_assets) / abs(prev_assets)
    
    # Get latest ratios
    latest_ratios = ratios_data[0] if ratios_data else {}
    
    return {
        # Stock info
        "name": profile.get("companyName", ""),
        "sector": profile.get("sector", ""),
        "industry": profile.get("industry", ""),
        "exchange": profile.get("exchange", ""),
        "currency": profile.get("currency", "USD"),
        
        # Value factors
        "pe_ratio": profile.get("pe"),
        "pb_ratio": profile.get("priceToBookRatio"),
        "ev_to_ebitda": latest_ratios.get("enterpriseValueMultiple"),
        "dividend_yield": profile.get("lastDiv"),
        "earnings_yield": 1 / profile.get("pe") if profile.get("pe") and profile.get("pe") > 0 else None,
        
        # Quality factors
        "roe": latest_ratios.get("returnOnEquity"),
        "roa": latest_ratios.get("returnOnAssets"),
        "gross_profitability": latest_ratios.get("grossProfitMargin"),
        "earnings_stability": latest_ratios.get("earningsStability"),
        "debt_to_equity": latest_ratios.get("debtEquityRatio"),
        
        # Growth factors
        "earnings_growth": earnings_growth,
        "sales_growth": sales_growth,
        "cash_flow_growth": cash_flow_growth,
        
        # Profitability factors
        "net_margin": latest_ratios.get("netProfitMargin"),
        "operating_margin": latest_ratios.get("operatingProfitMargin"),
        "free_cash_flow_yield": latest_ratios.get("freeCashFlowYield"),
        "roic": latest_ratios.get("returnOnCapitalEmployed"),
        
        # Investment factors
        "asset_growth_rate": asset_growth_rate,
        "capex_to_depreciation": latest_ratios.get("capexToDepreciation"),
        "rnd_to_sales": latest_ratios.get("researchAndDevelopmentToRevenue"),
        
        "last_updated": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
