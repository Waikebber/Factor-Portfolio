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
                    country, full_time_employees, is_actively_trading, is_adr, last_updated
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
            """, (
                data.get("symbol"),
                data.get("company_name"),
                data.get("exchange_short_name"),
                data.get("industry"),
                data.get("sector"),
                data.get("country"),
                data.get("full_time_employees"),
                data.get("is_actively_trading"),
                data.get("is_adr")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing stock: {e}")

    def store_employee_count(self, symbol: str, date: str, employee_count: int):
        """Store a row in the employee_count table."""
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO employee_count (
                    symbol, date, employee_count, last_updated
                ) VALUES (?, ?, ?, datetime('now'))
            """, (
                symbol,
                date,
                employee_count
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing employee count: {e}")
