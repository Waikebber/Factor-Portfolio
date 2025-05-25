import sqlite3
from typing import Dict, Any, List
import logging

class StoreMarketData:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = conn.cursor()

    def store_price(self, data: Dict[str, Any]):
        """
        Store price data from the processed data dictionary.
        
        Args:
            data: Dictionary containing price data with symbol and date keys
        """
        try:
            symbol = data.get('symbol')
            date = data.get('date')
            
            self.cursor.execute("""
                INSERT OR REPLACE INTO price (
                    symbol, date, open, high, low, close, volume,
                    change, change_percent, vwap
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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

    def store_dividend(self, data: Dict[str, Any]):
        """
        Store dividend data from the processed data dictionary.
        
        Args:
            data: Dictionary containing dividend data with symbol and date keys
        """
        try:
            symbol = data.get('symbol')
            date = data.get('date')
            
            self.cursor.execute("""
                INSERT OR REPLACE INTO dividends (
                    symbol, date, declaration_date, adj_dividend, dividend, yield, frequency
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
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

    def store_split(self, data: Dict[str, Any]):
        try:
            symbol = data.get('symbol')
            date = data.get('date')

            self.cursor.execute("""
                INSERT OR REPLACE INTO splits (
                    symbol, date, numerator, denominator
                ) VALUES (?, ?, ?, ?)
            """, (
                symbol,
                date,
                data.get("numerator"),
                data.get("denominator")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing split for {symbol} on {date}: {e}")

    def store_dividend_adjusted_price(self, data: Dict[str, Any]):
        """
        Store dividend adjusted price data from the processed data dictionary.
        
        Args:
            data: Dictionary containing dividend adjusted price data with symbol and date keys
        """
        try:
            symbol = data.get('symbol')
            date = data.get('date')
            
            self.cursor.execute("""
                INSERT OR REPLACE INTO dividend_adjusted_price_data (
                    symbol, date, adj_open, adj_high, adj_low, adj_close,
                    volume
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                symbol,
                date,
                data.get("adj_open"),
                data.get("adj_high"),
                data.get("adj_low"),
                data.get("adj_close"),
                data.get("volume")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing dividend adjusted price for {symbol} on {date}: {e}")

    def store_market_cap(self, data: Dict[str, Any]):
        try:
            symbol = data.get('symbol')
            date = data.get('date')

            self.cursor.execute("""
                INSERT OR REPLACE INTO market_cap (
                    symbol, date, market_cap
                ) VALUES (?, ?, ?)
            """, (
                symbol,
                date,
                data.get("market_cap")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing market cap for {symbol} on {date}: {e}")

    def store_share_float(self, data: Dict[str, Any]):
        """
        Store share float data from the processed data dictionary.
        
        Args:
            data: Dictionary containing share float data with symbol and date keys
        """
        try:
            if not isinstance(data, dict):
                logging.error(f"Invalid data format for share float: {type(data)}")
                return

            symbol = data.get('symbol')
            date = data.get('date')
            
            if not symbol or not date:
                logging.error(f"Missing required fields for share float: symbol={symbol}, date={date}")
                return

            self.cursor.execute("""
                INSERT OR REPLACE INTO share_float (
                    symbol, date, free_float, float_shares, outstanding_shares
                ) VALUES (?, ?, ?, ?, ?)
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
            logging.debug(f"Data received: {data}")
