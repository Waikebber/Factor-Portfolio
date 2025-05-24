import sqlite3
import pandas as pd
from typing import List, Optional, Tuple
from datetime import datetime

class StockDataGetter:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def get_price_data(self, tickers: List[str], start_date: Optional[datetime] = None, end_date: Optional[datetime] = None):
        query = "SELECT date, ticker, adjClose FROM daily_prices WHERE ticker IN ({})".format(','.join(['?'] * len(tickers)))
        params = tickers.copy()
        if start_date:
            query += " AND date >= ?"
            params.append(start_date.strftime('%Y-%m-%d'))
        if end_date:
            query += " AND date <= ?"
            params.append(end_date.strftime('%Y-%m-%d'))
        df = pd.read_sql_query(query, self.conn, params=params)
        df.index = pd.to_datetime(df['date'])
        return df.pivot(index='date', columns='ticker', values='adjClose')

    def get_available_tickers(self) -> List[str]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT ticker FROM daily_prices")
        return [row[0] for row in cursor.fetchall()]

    def get_data_range(self) -> Tuple[datetime, datetime]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT MIN(date), MAX(date) FROM daily_prices")
        start, end = cursor.fetchone()
        return pd.to_datetime(start), pd.to_datetime(end)

    def get_last_update(self) -> Optional[str]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT value FROM metadata WHERE key = 'last_update'")
        result = cursor.fetchone()
        return result[0] if result else None

    def update_last_update(self, timestamp: str) -> None:
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO metadata (key, value)
            VALUES (?, ?)
        ''', ('last_update', timestamp))
        self.conn.commit()
