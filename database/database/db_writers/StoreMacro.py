import sqlite3
import logging
from typing import Dict, Any

class StoreMacro:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = conn.cursor()

    def store_economic_indicators(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO economic_indicators (
                    name, date, value
                ) VALUES (?, ?, ?)
            """, (
                data.get("name"),
                data.get("date"),
                data.get("value")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing economic indicator for {data.get('name')} on {data.get('date')}: {e}")

    def store_industry_pe(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO industry_pe (
                    date, industry, exchange, pe
                ) VALUES (?, ?, ?, ?)
            """, (
                data.get("date"),
                data.get("industry"),
                data.get("exchange"),
                data.get("pe")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing industry PE for {data.get('industry')} on {data.get('date')}: {e}")

    def store_sector_pe(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO sector_pe (
                    date, sector, exchange, pe
                ) VALUES (?, ?, ?, ?)
            """, (
                data.get("date"),
                data.get("sector"),
                data.get("exchange"),
                data.get("pe")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing sector PE for {data.get('sector')} on {data.get('date')}: {e}")

    def store_industry_performance(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO industry_performance (
                    date, industry, exchange, average_change
                ) VALUES (?, ?, ?, ?)
            """, (
                data.get("date"),
                data.get("industry"),
                data.get("exchange"),
                data.get("average_change")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing industry performance for {data.get('industry')} on {data.get('date')}: {e}")

    def store_sector_performance(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO sector_performance (
                    date, sector, exchange, average_change
                ) VALUES (?, ?, ?, ?)
            """, (
                data.get("date"),
                data.get("sector"),
                data.get("exchange"),
                data.get("average_change")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing sector performance for {data.get('sector')} on {data.get('date')}: {e}")

    def store_treasury_rates(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO treasury_rates (
                    date, month_1, month_2, month_3, month_6, year_1, year_2, year_3, year_5, year_7, year_10, year_20, year_30
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                data.get("date"),
                data.get("month_1"),
                data.get("month_2"),
                data.get("month_3"),
                data.get("month_6"),
                data.get("year_1"),
                data.get("year_2"),
                data.get("year_3"),
                data.get("year_5"),
                data.get("year_7"),
                data.get("year_10"),
                data.get("year_20"),
                data.get("year_30")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing treasury rates for {data.get('date')}: {e}")
        
    def store_mergers_and_acquisitions(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO mergers_acquisitions (
                    symbol, targeted_symbol, transaction_date
                ) VALUES (?, ?, ?)
            """, (
                data.get("symbol"),
                data.get("targeted_symbol"),
                data.get("transaction_date")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing merger/acquisition for {data.get('symbol')}: {e}")
