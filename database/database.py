import sqlite3
import os, time
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any
from tqdm import tqdm
from .endpoints.fmp_fetch import fetch_historical_prices, fetch_fundamentals

class StockDatabase:
    """Class for managing stock data database operations."""

    def __init__(self, db_name='stock_data.db'):
        self.db_name = db_name
        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), db_name)
        self.max_retries = 3
        self.retry_delay = 30  # seconds between retries
        self.batch_size = 25  # FMP allows more requests per batch
        self.batch_delay = 60

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def initialize(self):
        try:
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            conn = self._get_connection()
            cursor = conn.cursor()

            # Load schema from external SQL file
            schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
            with open(schema_path, "r") as f:
                cursor.executescript(f.read())

            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error initializing database: {e}")
            return False

    def delete(self):
        try:
            if os.path.exists(self.db_path):
                os.remove(self.db_path)
            return True
        except Exception as e:
            print(f"Error deleting database: {e}")
            return False

    def get_last_update(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM metadata WHERE key = 'last_update'")
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

    def get_sp500_tickers(self):
        url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        tables = pd.read_html(url)
        df = tables[0]
        return df['Symbol'].tolist()

    def _download_with_retry(self, tickers: List[str], start_date: datetime, end_date: datetime) -> Optional[pd.DataFrame]:
        for attempt in range(self.max_retries):
            try:
                if attempt > 0:
                    print(f"Retry {attempt + 1} in {self.retry_delay} seconds...")
                    time.sleep(self.retry_delay)
                return fetch_historical_prices(tickers, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
        return None

    def _get_fundamental_data_with_retry(self, ticker: str) -> Optional[Dict[str, Any]]:
        for attempt in range(self.max_retries):
            try:
                if attempt > 0:
                    print(f"Retry {attempt + 1} for fundamentals...")
                    time.sleep(self.retry_delay)
                return fetch_fundamentals(ticker)
            except Exception as e:
                print(f"Fundamental data fetch failed for {ticker}: {e}")
        return None

    def update_stock_data(self, tickers: Optional[List[str]] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> bool:
        try:
            if tickers is None:
                tickers = self.get_sp500_tickers()
            if end_date is None:
                end_date = datetime.now()
            if start_date is None:
                start_date = end_date - timedelta(days=365 * 3)

            print(f"Starting download for {len(tickers)} tickers")
            num_batches = (len(tickers) + self.batch_size - 1) // self.batch_size
            with tqdm(total=len(tickers), desc="Overall Progress") as pbar:
                for i in range(0, len(tickers), self.batch_size):
                    batch = tickers[i:i + self.batch_size]
                    print(f"\nBatch {i // self.batch_size + 1} / {num_batches}: {batch}")
                    self._process_batch(batch, start_date, end_date)
                    pbar.update(len(batch))
                    if i + self.batch_size < len(tickers):
                        print(f"Sleeping for {self.batch_delay} seconds...")
                        time.sleep(self.batch_delay)

            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO metadata (key, value)
                VALUES (?, ?)
            ''', ('last_update', datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            conn.commit()
            conn.close()
            print("Update complete.")
            return True
        except Exception as e:
            print(f"Error updating stock data: {e}")
            return False

    def _process_batch(self, tickers: List[str], start_date: datetime, end_date: datetime) -> bool:
        try:
            price_data = self._download_with_retry(tickers, start_date, end_date)
            if price_data is None or price_data.empty:
                print("Price data is empty, skipping batch.")
                return False

            conn = self._get_connection()
            cursor = conn.cursor()

            # Store price data
            for ticker in tickers:
                if ticker not in price_data.columns:
                    continue
                adj_close = price_data[ticker].dropna()
                for date, value in adj_close.items():
                    cursor.execute('''
                        INSERT OR REPLACE INTO price_data (date, ticker, adj_close)
                        VALUES (?, ?, ?)
                    ''', (date.strftime('%Y-%m-%d'), ticker, float(value)))

            # Store fundamental data
            for ticker in tickers:
                fund = self._get_fundamental_data_with_retry(ticker)
                if fund:
                    cursor.execute('''
                        INSERT OR REPLACE INTO fundamental_data
                        (ticker, market_cap, pe_ratio, pb_ratio, dividend_yield, last_updated)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (
                        ticker,
                        fund['market_cap'],
                        fund['pe_ratio'],
                        fund['pb_ratio'],
                        fund['dividend_yield'],
                        fund['last_updated']
                    ))

            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error processing batch: {e}")
            return False

    def get_price_data(self, tickers, start_date=None, end_date=None):
        conn = self._get_connection()
        query = "SELECT date, ticker, adj_close FROM price_data WHERE ticker IN ({})".format(
            ','.join(['?'] * len(tickers))
        )
        params = tickers.copy()
        if start_date:
            query += " AND date >= ?"
            params.append(start_date.strftime('%Y-%m-%d'))
        if end_date:
            query += " AND date <= ?"
            params.append(end_date.strftime('%Y-%m-%d'))
        df = pd.read_sql_query(query, conn, params=params)
        df.index = pd.to_datetime(df['date'])
        result = df.pivot(index='date', columns='ticker', values='adj_close')
        conn.close()
        return result

    def get_fundamental_data(self, tickers):
        conn = self._get_connection()
        query = "SELECT * FROM fundamental_data WHERE ticker IN ({})".format(
            ','.join(['?'] * len(tickers))
        )
        df = pd.read_sql_query(query, conn, params=tickers, index_col='ticker')
        conn.close()
        return df

    def get_available_tickers(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT ticker FROM price_data")
        tickers = [row[0] for row in cursor.fetchall()]
        conn.close()
        return tickers

    def get_data_range(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT MIN(date), MAX(date) FROM price_data")
        start, end = cursor.fetchone()
        conn.close()
        return pd.to_datetime(start), pd.to_datetime(end)

    def prepare_alpha_data(self, factor_df, returns, lookback=252):
        X = factor_df.shift(1).dropna()
        y = returns.shift(-1).loc[X.index]
        split = int(len(X) * 0.8)
        return X[:split], X[split:], y[:split], y[split:]

if __name__ == "__main__":
    db = StockDatabase()
    db.initialize()
    db.update_stock_data()
