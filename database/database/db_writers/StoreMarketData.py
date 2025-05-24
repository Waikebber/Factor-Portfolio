import sqlite3
from typing import Dict, Any, List
import logging

class StoreMarketData:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = conn.cursor()

    def store_price(self, symbol: str, date: str, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO price (
                    symbol, date, open, high, low, close, volume,
                    change, change_percent, vwap, last_updated
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
            """, (
                symbol,
                date,
                data.get("open"),
                data.get("high"),
                data.get("low"),
                data.get("close"),
                data.get("volume"),
                data.get("change"),
                data.get("change_percent"),
                data.get("vwap")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing price for {symbol} on {date}: {e}")

    def store_dividend(self, symbol: str, date: str, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO dividends (
                    symbol, date, declaration_date, adj_dividend, dividend, yield, frequency, last_updated
                ) VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))
            """, (
                symbol,
                date,
                data.get("declaration_date"),
                data.get("adj_dividend"),
                data.get("dividend"),
                data.get("yield"),
                data.get("frequency")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing dividend for {symbol} on {date}: {e}")

    def store_split(self, symbol: str, date: str, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO splits (
                    symbol, date, numerator, denominator, last_updated
                ) VALUES (?, ?, ?, ?, datetime('now'))
            """, (
                symbol,
                date,
                data.get("numerator"),
                data.get("denominator")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing split for {symbol} on {date}: {e}")

    def store_dividend_adjusted_price(self, symbol: str, date: str, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO dividend_adjusted_price_data (
                    symbol, date, open, high, low, close, adj_open, adj_high, adj_low, adj_close,
                    volume, unadjusted_volume, change, change_percent, vwap, label, change_over_time, last_updated
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
            """, (
                symbol,
                date,
                data.get("open"),
                data.get("high"),
                data.get("low"),
                data.get("close"),
                data.get("adj_open"),
                data.get("adj_high"),
                data.get("adj_low"),
                data.get("adj_close"),
                data.get("volume"),
                data.get("unadjusted_volume"),
                data.get("change"),
                data.get("change_percent"),
                data.get("vwap"),
                data.get("label"),
                data.get("change_over_time")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing dividend adjusted price for {symbol} on {date}: {e}")

    def store_market_cap(self, symbol: str, date: str, market_cap: float):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO market_cap (
                    symbol, date, market_cap, last_updated
                ) VALUES (?, ?, ?, datetime('now'))
            """, (
                symbol,
                date,
                market_cap
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing market cap for {symbol} on {date}: {e}")

    def store_share_float(self, symbol: str, date: str, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO share_float (
                    symbol, date, free_float, float_shares, outstanding_shares, last_updated
                ) VALUES (?, ?, ?, ?, ?, datetime('now'))
            """, (
                symbol,
                date,
                data.get("free_float"),
                data.get("float_shares"),
                data.get("outstanding_shares")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing share float for {symbol} on {date}: {e}")

    def store_dividend_adjusted_prices(self, ticker: str, data: Dict[str, Any]):
        """Store dividend-adjusted price data."""
        try:
            self.cursor.execute("""
                INSERT INTO dividend_adjusted_price_data (
                    symbol, date, adjusted_close, last_updated
                ) VALUES (?, ?, ?, datetime('now'))
            """, (
                ticker,
                data.get("date"),
                data.get("adjusted_close")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing dividend-adjusted prices for {ticker}: {e}")

    def store_dividends(self, ticker: str, data: List[Dict[str, Any]]):
        """Store dividend data."""
        try:
            for dividend in data:
                self.cursor.execute("""
                    INSERT INTO dividends (
                        symbol, date, amount, last_updated
                    ) VALUES (?, ?, ?, datetime('now'))
                """, (
                    ticker,
                    dividend.get("date"),
                    dividend.get("amount")
                ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing dividends for {ticker}: {e}")

    def store_splits(self, ticker: str, data: List[Dict[str, Any]]):
        """Store stock split data."""
        try:
            for split in data:
                self.cursor.execute("""
                    INSERT INTO splits (
                        symbol, date, ratio, last_updated
                    ) VALUES (?, ?, ?, datetime('now'))
                """, (
                    ticker,
                    split.get("date"),
                    split.get("ratio")
                ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing splits for {ticker}: {e}")
