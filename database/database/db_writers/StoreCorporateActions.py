import sqlite3
import logging
from typing import Dict, Any

class StoreCorporateActions:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = conn.cursor()

    def store_merger_acquisition(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO mergers_acquisitions (
                    symbol, targeted_symbol, transaction_date, last_updated
                ) VALUES (?, ?, ?, datetime('now'))
            """, (
                data.get("symbol"),
                data.get("targeted_symbol"),
                data.get("transaction_date")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing merger/acquisition for {data.get('symbol')}: {e}")

    def store_earnings(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO earnings (
                    symbol, date, eps_actual, eps_estimated, revenue_actual, revenue_estimated, last_updated
                ) VALUES (?, ?, ?, ?, ?, ?, datetime('now'))
            """, (
                data.get("symbol"),
                data.get("date"),
                data.get("eps_actual"),
                data.get("eps_estimated"),
                data.get("revenue_actual"),
                data.get("revenue_estimated")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing earnings for {data.get('symbol')} on {data.get('date')}: {e}")
