import argparse
from datetime import datetime, timedelta
from typing import List, Dict, Any
import pandas as pd
from database import StockDatabase
from .endpoints.fmp_fetch import fetch_historical_prices, fetch_fundamentals

def store_prices(db: StockDatabase, df, tickers: List[str]):
    conn = db._get_connection()
    cursor = conn.cursor()
    
    for date in df.index:
        for ticker in tickers:
            value = df.at[date, ticker]
            if pd.notna(value):
                cursor.execute('''
                    INSERT OR REPLACE INTO price_data (date, ticker, adj_close)
                    VALUES (?, ?, ?)
                ''', (date.strftime('%Y-%m-%d'), ticker, float(value)))
    
    conn.commit()
    conn.close()

def store_stock_info(db: StockDatabase, ticker: str, data: Dict[str, Any]):
    conn = db._get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO stocks (ticker, name, sector, industry, exchange, currency)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        ticker,
        data.get('name', ''),
        data.get('sector', ''),
        data.get('industry', ''),
        data.get('exchange', ''),
        data.get('currency', 'USD')
    ))
    conn.commit()
    conn.close()

def store_value_factors(db: StockDatabase, ticker: str, data: Dict[str, Any]):
    conn = db._get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO value_factors 
        (ticker, pe_ratio, pb_ratio, ev_to_ebitda, dividend_yield, earnings_yield, last_updated)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        ticker,
        data.get('pe_ratio'),
        data.get('pb_ratio'),
        data.get('ev_to_ebitda'),
        data.get('dividend_yield'),
        data.get('earnings_yield'),
        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ))
    conn.commit()
    conn.close()

def store_quality_factors(db: StockDatabase, ticker: str, data: Dict[str, Any]):
    conn = db._get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO quality_factors 
        (ticker, roe, roa, gross_profitability, earnings_stability, debt_to_equity, last_updated)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        ticker,
        data.get('roe'),
        data.get('roa'),
        data.get('gross_profitability'),
        data.get('earnings_stability'),
        data.get('debt_to_equity'),
        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ))
    conn.commit()
    conn.close()

def store_growth_factors(db: StockDatabase, ticker: str, data: Dict[str, Any]):
    conn = db._get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO growth_factors 
        (ticker, earnings_growth, sales_growth, cash_flow_growth, last_updated)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        ticker,
        data.get('earnings_growth'),
        data.get('sales_growth'),
        data.get('cash_flow_growth'),
        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ))
    conn.commit()
    conn.close()

def store_profitability_factors(db: StockDatabase, ticker: str, data: Dict[str, Any]):
    conn = db._get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO profitability_factors 
        (ticker, net_margin, operating_margin, free_cash_flow_yield, roic, last_updated)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        ticker,
        data.get('net_margin'),
        data.get('operating_margin'),
        data.get('free_cash_flow_yield'),
        data.get('roic'),
        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ))
    conn.commit()
    conn.close()

def store_investment_factors(db: StockDatabase, ticker: str, data: Dict[str, Any]):
    conn = db._get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO investment_factors 
        (ticker, asset_growth_rate, capex_to_depreciation, rnd_to_sales, last_updated)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        ticker,
        data.get('asset_growth_rate'),
        data.get('capex_to_depreciation'),
        data.get('rnd_to_sales'),
        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ))
    conn.commit()
    conn.close()

def populate_database(force_update=False, days_back=365*3):
    db = StockDatabase()
    if not db.initialize():
        print("Failed to initialize database")
        return

    tickers = db.get_sp500_tickers()
    print(f"Found {len(tickers)} S&P 500 tickers")

    end_date = datetime.now()
    start_date = end_date - timedelta(days=days_back)

    last_update = db.get_last_update()
    if last_update and not force_update:
        last_update = datetime.strptime(last_update, '%Y-%m-%d %H:%M:%S')
        if (end_date - last_update).days < 1:
            print(f"Database is up to date (last updated: {last_update})")
            return

    batch_size = db.batch_size
    for i in range(0, len(tickers), batch_size):
        batch = tickers[i:i + batch_size]
        print(f"\nProcessing batch {i // batch_size + 1}: {batch}")
        try:
            # Fetch and store price data
            df = fetch_historical_prices(batch, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
            if not df.empty:
                store_prices(db, df, batch)

            # Fetch and store fundamental data for each ticker
            for ticker in batch:
                fundamentals = fetch_fundamentals(ticker)
                if fundamentals:
                    store_stock_info(db, ticker, fundamentals)
                    store_value_factors(db, ticker, fundamentals)
                    store_quality_factors(db, ticker, fundamentals)
                    store_growth_factors(db, ticker, fundamentals)
                    store_profitability_factors(db, ticker, fundamentals)
                    store_investment_factors(db, ticker, fundamentals)

        except Exception as e:
            print(f"Error processing batch {batch}: {e}")

    conn = db._get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO metadata (key, value)
        VALUES (?, ?)
    ''', ('last_update', datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    conn.close()
    print("Database update completed.")

def main():
    parser = argparse.ArgumentParser(description='Populate or update the stock database')
    parser.add_argument('--force', action='store_true', help='Force update all data')
    parser.add_argument('--days', type=int, default=365*3, help='Number of days of historical data to download')
    args = parser.parse_args()

    populate_database(args.force, args.days)

if __name__ == "__main__":
    main()
