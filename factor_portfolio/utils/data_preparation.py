"""
Data preparation utilities.
"""

import pandas as pd
import numpy as np
import yfinance as yf

def get_sp500_tickers():
    """Get S&P 500 tickers from Wikipedia.
    
    Returns:
        list: List of S&P 500 ticker symbols
    """
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    tables = pd.read_html(url)
    df = tables[0]
    return df['Symbol'].tolist()

def download_data(tickers, start_date, end_date):
    """Download price and fundamental data for given tickers.
    
    Args:
        tickers (list): List of ticker symbols
        start_date (datetime): Start date
        end_date (datetime): End date
        
    Returns:
        tuple: (price_data, fundamental_data)
    """
    # Download price data
    price_data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    
    # Download fundamental data
    fundamental_data = {}
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            fundamental_data[ticker] = {
                'market_cap': info.get('marketCap', np.nan),
                'pe_ratio': info.get('trailingPE', np.nan),
                'pb_ratio': info.get('priceToBook', np.nan),
                'dividend_yield': info.get('dividendYield', np.nan)
            }
        except:
            continue
    
    return price_data, pd.DataFrame(fundamental_data).T

def prepare_alpha_data(factor_df, returns, lookback=252):
    """Prepare data for alpha modeling.
    
    Args:
        factor_df (pd.DataFrame): Factor scores
        returns (pd.DataFrame): Asset returns
        lookback (int): Lookback period in days
        
    Returns:
        tuple: (X_train, X_test, y_train, y_test)
    """
    # Align factor scores with future returns
    X = factor_df.shift(1).dropna()  # Features
    y = returns.shift(-1).loc[X.index]  # Target (next period returns)
    
    # Split into training and testing sets
    train_size = int(len(X) * 0.8)
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    
    return X_train, X_test, y_train, y_test 