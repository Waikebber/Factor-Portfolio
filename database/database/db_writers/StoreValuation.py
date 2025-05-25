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
                    symbol, date, stock_price, number_of_shares, market_capitalization,
                    minus_cash_and_cash_equivalents, add_total_debt, enterprise_value
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                data.get("symbol"),
                data.get("date"),
                data.get("stock_price"),
                data.get("number_of_shares"),
                data.get("market_capitalization"),
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
                    symbol, date, fiscal_year, period, reported_currency,
                    average_ppe, maintenance_capex, owners_earnings, growth_capex,
                    owners_earnings_per_share
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                data.get("symbol"),
                data.get("date"),
                data.get("fiscal_year"),
                data.get("period"),
                data.get("reported_currency"),
                data.get("average_ppe"),
                data.get("maintenance_capex"),
                data.get("owners_earnings"),
                data.get("growth_capex"),
                data.get("owners_earnings_per_share")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing owner earnings for {data.get('symbol')} on {data.get('date')}: {e}")

    def store_levered_discounted_cash_flow(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO levered_discounted_cash_flow (
                    symbol, date, dcf, stock_price
                ) VALUES (?, ?, ?, ?)
            """, (
                data.get("symbol"),
                data.get("date"),
                data.get("dcf"),
                data.get("stock_price")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing levered discounted cash flow for {data.get('symbol')} on {data.get('date')}: {e}")

    def store_discounted_cash_flow(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO discounted_cash_flow (
                    symbol, date, dcf, stock_price
                ) VALUES (?, ?, ?, ?)
            """, (
                data.get("symbol"),
                data.get("date"),
                data.get("dcf"),
                data.get("stock_price")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing discounted cash flow for {data.get('symbol')} on {data.get('date')}: {e}")
