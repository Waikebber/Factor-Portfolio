import sqlite3
import logging
from typing import Dict, Any

class StoreCore:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = conn.cursor()

    def store_stock(self, data: Dict[str, Any]):
        """Store a row in the stocks table."""
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO stocks (
                    symbol, company_name, exchange_short_name, industry, sector,
                    country, is_actively_trading, last_updated
                ) VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))
            """, (
                data.get("symbol"),
                data.get("company_name"),
                data.get("exchange_short_name"),
                data.get("industry"),
                data.get("sector"),
                data.get("country"),
                data.get("is_actively_trading"),
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing stock: {e}")

    def store_employee_count(self, data: Dict[str, Any]):
        """Store a row in the employee_count table.
        
        Args:
            data: Dictionary containing 'symbol', 'date', and 'employee_count' keys
        """
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO employee_count (
                    symbol, date, employee_count
                ) VALUES (?, ?, ?)
            """, (
                data.get('symbol'),
                data.get('date'),
                data.get('employee_count')
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing employee count: {e}")
