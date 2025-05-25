import sqlite3
import logging
from typing import Dict, Any

class StoreAnalysisData:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = conn.cursor()

    def store_grades_consensus(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO grades_consensus (
                    symbol, strong_buy, buy, hold, sell, strong_sell, consensus, last_updated
                ) VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))
            """, (
                data.get("symbol"),
                data.get("strong_buy"),
                data.get("buy"),
                data.get("hold"),
                data.get("sell"),
                data.get("strong_sell"),
                data.get("consensus")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing grades consensus for {data.get('symbol')}: {e}")

    def store_grades(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO grades (
                    symbol, date, buy, hold, sell, strong_sell
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                data.get("symbol"),
                data.get("date"),
                data.get("buy"),
                data.get("hold"),
                data.get("sell"),
                data.get("strong_sell")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing grades for {data.get('symbol')} on {data.get('date')}: {e}")

    def store_price_target_consensus(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO price_target_consensus (
                    symbol, target_high, target_low, target_consensus, target_median, last_updated
                ) VALUES (?, ?, ?, ?, ?, datetime('now'))
            """, (
                data.get("symbol"),
                data.get("target_high"),
                data.get("target_low"),
                data.get("target_consensus"),
                data.get("target_median")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing price target consensus for {data.get('symbol')}: {e}")

    def store_price_target_summary(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO price_target_summary (
                    symbol, last_month_count, last_month_avg_price_target, last_quarter_count, last_quarter_avg_price_target,
                    last_year_count, last_year_avg_price_target, all_time_count, all_time_avg_price_target, last_updated
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
            """, (
                data.get("symbol"),
                data.get("last_month_count"),
                data.get("last_month_avg_price_target"),
                data.get("last_quarter_count"),
                data.get("last_quarter_avg_price_target"),
                data.get("last_year_count"),
                data.get("last_year_avg_price_target"),
                data.get("all_time_count"),
                data.get("all_time_avg_price_target")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing price target summary for {data.get('symbol')}: {e}")
