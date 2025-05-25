import sqlite3
import logging
from typing import Dict, Any

class StoreFinancialMetrics:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = conn.cursor()

    def store_financial_ratios(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO financial_ratios (
                    symbol, date, fiscal_year, period, reported_currency,
                    gross_profit_margin, ebit_margin, ebitda_margin, operating_profit_margin,
                    pretax_profit_margin, continuous_operations_profit_margin, net_profit_margin,
                    bottom_line_profit_margin, receivables_turnover, payables_turnover,
                    inventory_turnover, fixed_asset_turnover, asset_turnover, current_ratio,
                    quick_ratio, solvency_ratio, cash_ratio, price_to_earnings_ratio,
                    price_to_earnings_growth_ratio, forward_price_to_earnings_growth_ratio,
                    price_to_book_ratio, price_to_sales_ratio, price_to_free_cash_flow_ratio,
                    price_to_operating_cash_flow_ratio, debt_to_assets_ratio,
                    debt_to_equity_ratio, debt_to_capital_ratio, long_term_debt_to_capital_ratio,
                    financial_leverage_ratio, debt_to_market_cap, working_capital_turnover_ratio,
                    operating_cash_flow_ratio, operating_cash_flow_sales_ratio,
                    free_cash_flow_operating_cash_flow_ratio, debt_service_coverage_ratio,
                    interest_coverage_ratio, short_term_operating_cash_flow_coverage_ratio,
                    operating_cash_flow_coverage_ratio, capital_expenditure_coverage_ratio,
                    dividend_paid_and_capex_coverage_ratio, dividend_payout_ratio,
                    dividend_yield, dividend_yield_percentage, revenue_per_share,
                    net_income_per_share, interest_debt_per_share, cash_per_share,
                    book_value_per_share, tangible_book_value_per_share,
                    shareholders_equity_per_share, operating_cash_flow_per_share,
                    capex_per_share, free_cash_flow_per_share, net_income_per_ebt,
                    ebt_per_ebit, price_to_fair_value, effective_tax_rate,
                    enterprise_value_multiple
                ) VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
            """, (
                data.get("symbol"), data.get("date"), data.get("fiscal_year"), data.get("period"), data.get("reported_currency"),
                data.get("gross_profit_margin"), data.get("ebit_margin"), data.get("ebitda_margin"), data.get("operating_profit_margin"),
                data.get("pretax_profit_margin"), data.get("continuous_operations_profit_margin"), data.get("net_profit_margin"),
                data.get("bottom_line_profit_margin"), data.get("receivables_turnover"), data.get("payables_turnover"),
                data.get("inventory_turnover"), data.get("fixed_asset_turnover"), data.get("asset_turnover"), data.get("current_ratio"),
                data.get("quick_ratio"), data.get("solvency_ratio"), data.get("cash_ratio"), data.get("price_to_earnings_ratio"),
                data.get("price_to_earnings_growth_ratio"), data.get("forward_price_to_earnings_growth_ratio"),
                data.get("price_to_book_ratio"), data.get("price_to_sales_ratio"), data.get("price_to_free_cash_flow_ratio"),
                data.get("price_to_operating_cash_flow_ratio"), data.get("debt_to_assets_ratio"), data.get("debt_to_equity_ratio"),
                data.get("debt_to_capital_ratio"), data.get("long_term_debt_to_capital_ratio"), data.get("financial_leverage_ratio"),
                data.get("debt_to_market_cap"), data.get("working_capital_turnover_ratio"), data.get("operating_cash_flow_ratio"),
                data.get("operating_cash_flow_sales_ratio"), data.get("free_cash_flow_operating_cash_flow_ratio"),
                data.get("debt_service_coverage_ratio"), data.get("interest_coverage_ratio"),
                data.get("short_term_operating_cash_flow_coverage_ratio"), data.get("operating_cash_flow_coverage_ratio"),
                data.get("capital_expenditure_coverage_ratio"), data.get("dividend_paid_and_capex_coverage_ratio"),
                data.get("dividend_payout_ratio"), data.get("dividend_yield"), data.get("dividend_yield_percentage"),
                data.get("revenue_per_share"), data.get("net_income_per_share"), data.get("interest_debt_per_share"),
                data.get("cash_per_share"), data.get("book_value_per_share"), data.get("tangible_book_value_per_share"),
                data.get("shareholders_equity_per_share"), data.get("operating_cash_flow_per_share"),
                data.get("capex_per_share"), data.get("free_cash_flow_per_share"), data.get("net_income_per_ebt"),
                data.get("ebt_per_ebit"), data.get("price_to_fair_value"), data.get("effective_tax_rate"),
                data.get("enterprise_value_multiple")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing financial ratios for {data.get('symbol')} on {data.get('date')}: {e}")

    def store_key_metrics(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO key_metrics (
                    symbol, date, fiscal_year, period, reported_currency,
                    market_cap, enterprise_value, ev_to_sales, ev_to_operating_cash_flow,
                    ev_to_free_cash_flow, ev_to_ebitda, net_debt_to_ebitda, current_ratio,
                    income_quality, graham_number, graham_net_net, tax_burden,
                    interest_burden, working_capital, invested_capital, return_on_assets,
                    operating_return_on_assets, return_on_tangible_assets, return_on_equity,
                    return_on_invested_capital, return_on_capital_employed, earnings_yield,
                    free_cash_flow_yield, capex_to_operating_cash_flow, capex_to_depreciation,
                    capex_to_revenue, sga_to_revenue, rnd_to_revenue, sbc_to_revenue,
                    intangibles_to_total_assets, average_receivables, average_payables,
                    average_inventory, dso, dpo, dio, operating_cycle, cash_conversion_cycle,
                    fcf_to_equity, fcf_to_firm, tangible_asset_value, net_current_asset_value
                ) VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
            """, (
                data.get("symbol"), data.get("date"), data.get("fiscal_year"), data.get("period"), data.get("reported_currency"),
                data.get("market_cap"), data.get("enterprise_value"), data.get("ev_to_sales"), data.get("ev_to_operating_cash_flow"),
                data.get("ev_to_free_cash_flow"), data.get("ev_to_ebitda"), data.get("net_debt_to_ebitda"), data.get("current_ratio"),
                data.get("income_quality"), data.get("graham_number"), data.get("graham_net_net"), data.get("tax_burden"),
                data.get("interest_burden"), data.get("working_capital"), data.get("invested_capital"), data.get("return_on_assets"),
                data.get("operating_return_on_assets"), data.get("return_on_tangible_assets"), data.get("return_on_equity"),
                data.get("return_on_invested_capital"), data.get("return_on_capital_employed"), data.get("earnings_yield"),
                data.get("free_cash_flow_yield"), data.get("capex_to_operating_cash_flow"), data.get("capex_to_depreciation"),
                data.get("capex_to_revenue"), data.get("sga_to_revenue"), data.get("rnd_to_revenue"),
                data.get("sbc_to_revenue"), data.get("intangibles_to_total_assets"), data.get("average_receivables"),
                data.get("average_payables"), data.get("average_inventory"), data.get("dso"), data.get("dpo"),
                data.get("dio"), data.get("operating_cycle"), data.get("cash_conversion_cycle"),
                data.get("fcf_to_equity"), data.get("fcf_to_firm"), data.get("tangible_asset_value"),
                data.get("net_current_asset_value")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing key metrics for {data.get('symbol')} on {data.get('date')}: {e}")
        
    def store_earnings(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO earnings (
                    symbol, date, eps_actual, eps_estimated, revenue_actual, revenue_estimated
                ) VALUES (?, ?, ?, ?, ?, ?)
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
