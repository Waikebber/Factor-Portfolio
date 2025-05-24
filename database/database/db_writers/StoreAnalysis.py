import sqlite3
import logging
from typing import Dict, Any

class StoreAnalysis:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = conn.cursor()

    def store_ratings(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO ratings (
                    symbol, date, rating, overall_score, discounted_cash_flow_score,
                    return_on_equity_score, return_on_assets_score, debt_to_equity_score,
                    price_to_earnings_score, price_to_book_score, last_updated
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
            """, (
                data.get("symbol"),
                data.get("date"),
                data.get("rating"),
                data.get("overall_score"),
                data.get("discounted_cash_flow_score"),
                data.get("return_on_equity_score"),
                data.get("return_on_assets_score"),
                data.get("debt_to_equity_score"),
                data.get("price_to_earnings_score"),
                data.get("price_to_book_score")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing rating for {data.get('symbol')}: {e}")

    def store_analyst_estimates(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO analyst_estimates (
                    symbol, date, revenue_low, revenue_high, revenue_avg,
                    ebitda_low, ebitda_high, ebitda_avg, ebit_low, ebit_high, ebit_avg,
                    net_income_low, net_income_high, net_income_avg,
                    sga_expense_low, sga_expense_high, sga_expense_avg,
                    eps_low, eps_high, eps_avg, num_analysts_revenue, num_analysts_eps, last_updated
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
            """, (
                data.get("symbol"),
                data.get("date"),
                data.get("revenue_low"),
                data.get("revenue_high"),
                data.get("revenue_avg"),
                data.get("ebitda_low"),
                data.get("ebitda_high"),
                data.get("ebitda_avg"),
                data.get("ebit_low"),
                data.get("ebit_high"),
                data.get("ebit_avg"),
                data.get("net_income_low"),
                data.get("net_income_high"),
                data.get("net_income_avg"),
                data.get("sga_expense_low"),
                data.get("sga_expense_high"),
                data.get("sga_expense_avg"),
                data.get("eps_low"),
                data.get("eps_high"),
                data.get("eps_avg"),
                data.get("num_analysts_revenue"),
                data.get("num_analysts_eps")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing analyst estimate for {data.get('symbol')} on {data.get('date')}: {e}")
