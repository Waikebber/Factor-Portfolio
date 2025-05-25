import sqlite3
import logging
from typing import Dict, Any

class StoreValuation:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = conn.cursor()

    def store_enterprise_values(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO enterprise_values (
                    symbol, date, number_of_shares,
                    minus_cash_and_cash_equivalents, add_total_debt, enterprise_value
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                data.get("symbol"),
                data.get("date"),
                data.get("number_of_shares"),
                data.get("minus_cash_and_cash_equivalents"),
                data.get("add_total_debt"),
                data.get("enterprise_value")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing enterprise values for {data.get('symbol')} on {data.get('date')}: {e}")

    def store_owner_earnings(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO owner_earnings (
                    symbol, date, period, fiscal_year, avg_ppe,
                    growth_capex, maintenance_capex, owners_earnings,
                    owners_earnings_per_share
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                data.get("symbol"),
                data.get("date"),
                data.get("period"),
                data.get("fiscal_year"),
                data.get("avg_ppe"),
                data.get("growth_capex"),
                data.get("maintenance_capex"),
                data.get("owners_earnings"),
                data.get("owners_earnings_per_share")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing owner earnings for {data.get('symbol')} on {data.get('date')}: {e}")

    def store_levered_discounted_cash_flow(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO levered_discounted_cash_flow (
                    symbol, date, dcf
                ) VALUES (?, ?, ?)
            """, (
                data.get("symbol"),
                data.get("date"),
                data.get("dcf"),
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing levered discounted cash flow for {data.get('symbol')} on {data.get('date')}: {e}")

    def store_discounted_cash_flow(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO discounted_cash_flow (
                    symbol, date, dcf
                ) VALUES (?, ?, ?)
            """, (
                data.get("symbol"),
                data.get("date"),
                data.get("dcf"),
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing discounted cash flow for {data.get('symbol')} on {data.get('date')}: {e}")
