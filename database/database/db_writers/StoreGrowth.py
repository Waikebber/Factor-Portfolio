import sqlite3
import logging
from typing import Dict, Any

class StoreGrowth:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = conn.cursor()

    def store_balance_sheet_growth(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO balance_sheet_growth (
                    symbol, date, fiscal_year, period, reported_currency,
                    cash_and_cash_equivalents, short_term_investments, cash_and_short_term_investments,
                    net_receivables, inventory, other_current_assets, total_current_assets,
                    property_plant_equipment_net, goodwill, intangible_assets, goodwill_and_intangible_assets,
                    long_term_investments, tax_assets, other_non_current_assets, total_non_current_assets,
                    other_assets, total_assets, account_payables, short_term_debt, tax_payables,
                    deferred_revenue, other_current_liabilities, total_current_liabilities, long_term_debt,
                    deferred_revenue_non_current, deferred_tax_liabilities_non_current, other_non_current_liabilities,
                    total_non_current_liabilities, other_liabilities, total_liabilities, preferred_stock,
                    common_stock, retained_earnings, accumulated_other_comprehensive_income_loss,
                    other_total_stockholders_equity, total_stockholders_equity, minority_interest, total_equity,
                    total_liabilities_and_stockholders_equity, total_investments, total_debt, net_debt,
                    accounts_receivables, other_receivables, prepaids, total_payables, other_payables,
                    accrued_expenses, capital_lease_obligations_current, additional_paid_in_capital,
                    treasury_stock
                ) VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
            """, (
                data.get("symbol"), data.get("date"), data.get("fiscal_year"), data.get("period"), data.get("reported_currency"),
                data.get("cash_and_cash_equivalents"), data.get("short_term_investments"), data.get("cash_and_short_term_investments"),
                data.get("net_receivables"), data.get("inventory"), data.get("other_current_assets"), data.get("total_current_assets"),
                data.get("property_plant_equipment_net"), data.get("goodwill"), data.get("intangible_assets"), data.get("goodwill_and_intangible_assets"),
                data.get("long_term_investments"), data.get("tax_assets"), data.get("other_non_current_assets"), data.get("total_non_current_assets"),
                data.get("other_assets"), data.get("total_assets"), data.get("account_payables"), data.get("short_term_debt"), data.get("tax_payables"),
                data.get("deferred_revenue"), data.get("other_current_liabilities"), data.get("total_current_liabilities"), data.get("long_term_debt"),
                data.get("deferred_revenue_non_current"), data.get("deferred_tax_liabilities_non_current"), data.get("other_non_current_liabilities"),
                data.get("total_non_current_liabilities"), data.get("other_liabilities"), data.get("total_liabilities"), data.get("preferred_stock"),
                data.get("common_stock"), data.get("retained_earnings"), data.get("accumulated_other_comprehensive_income_loss"),
                data.get("other_total_stockholders_equity"), data.get("total_stockholders_equity"), data.get("minority_interest"), data.get("total_equity"),
                data.get("total_liabilities_and_stockholders_equity"), data.get("total_investments"), data.get("total_debt"), data.get("net_debt"),
                data.get("accounts_receivables"), data.get("other_receivables"), data.get("prepaids"), data.get("total_payables"), data.get("other_payables"),
                data.get("accrued_expenses"), data.get("capital_lease_obligations_current"), data.get("additional_paid_in_capital"),
                data.get("treasury_stock")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing balance sheet growth for {data.get('symbol')} on {data.get('date')}: {e}")

    def store_cashflow_statement_growth(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO cashflow_statement_growth (
                    symbol, date, fiscal_year, period, reported_currency,
                    net_income, depreciation_and_amortization, deferred_income_tax,
                    stock_based_compensation, change_in_working_capital, accounts_receivables,
                    inventory, accounts_payables, other_working_capital, other_non_cash_items,
                    net_cash_provided_by_operating_activites, investments_in_property_plant_and_equipment,
                    acquisitions_net, purchases_of_investments, sales_maturities_of_investments,
                    other_investing_activites, net_cash_used_for_investing_activites, debt_repayment,
                    common_stock_issued, common_stock_repurchased, dividends_paid,
                    other_financing_activites, net_cash_used_provided_by_financing_activities,
                    effect_of_forex_changes_on_cash, net_change_in_cash, cash_at_end_of_period,
                    cash_at_beginning_of_period, operating_cash_flow, capital_expenditure,
                    free_cash_flow, net_debt_issuance, long_term_net_debt_issuance,
                    short_term_net_debt_issuance, net_stock_issuance, preferred_dividends_paid,
                    income_taxes_paid, interest_paid
                ) VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
            """, (
                data.get("symbol"), data.get("date"), data.get("fiscal_year"), data.get("period"), data.get("reported_currency"),
                data.get("net_income"), data.get("depreciation_and_amortization"), data.get("deferred_income_tax"),
                data.get("stock_based_compensation"), data.get("change_in_working_capital"), data.get("accounts_receivables"),
                data.get("inventory"), data.get("accounts_payables"), data.get("other_working_capital"),
                data.get("other_non_cash_items"), data.get("net_cash_provided_by_operating_activites"),
                data.get("investments_in_property_plant_and_equipment"), data.get("acquisitions_net"),
                data.get("purchases_of_investments"), data.get("sales_maturities_of_investments"),
                data.get("other_investing_activites"), data.get("net_cash_used_for_investing_activites"),
                data.get("debt_repayment"), data.get("common_stock_issued"), data.get("common_stock_repurchased"),
                data.get("dividends_paid"), data.get("other_financing_activites"),
                data.get("net_cash_used_provided_by_financing_activities"), data.get("effect_of_forex_changes_on_cash"),
                data.get("net_change_in_cash"), data.get("cash_at_end_of_period"), data.get("cash_at_beginning_of_period"),
                data.get("operating_cash_flow"), data.get("capital_expenditure"), data.get("free_cash_flow"),
                data.get("net_debt_issuance"), data.get("long_term_net_debt_issuance"),
                data.get("short_term_net_debt_issuance"), data.get("net_stock_issuance"),
                data.get("preferred_dividends_paid"), data.get("income_taxes_paid"), data.get("interest_paid")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing cashflow statement growth for {data.get('symbol')} on {data.get('date')}: {e}")

    def store_financial_statement_growth(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO financial_statement_growth (
                    symbol, date, fiscal_year, period, reported_currency,
                    revenue_growth, gross_profit_growth, ebit_growth, operating_income_growth,
                    net_income_growth, eps_growth, eps_diluted_growth, weighted_average_shares_growth,
                    weighted_average_shares_diluted_growth, dividends_per_share_growth, operating_cash_flow_growth,
                    receivables_growth, inventory_growth, asset_growth, book_value_per_share_growth,
                    debt_growth, rd_expense_growth, sga_expenses_growth, free_cash_flow_growth,
                    ten_y_revenue_growth_per_share, five_y_revenue_growth_per_share, three_y_revenue_growth_per_share,
                    ten_y_operating_cf_growth_per_share, five_y_operating_cf_growth_per_share, three_y_operating_cf_growth_per_share,
                    ten_y_net_income_growth_per_share, five_y_net_income_growth_per_share, three_y_net_income_growth_per_share,
                    ten_y_shareholders_equity_growth_per_share, five_y_shareholders_equity_growth_per_share,
                    three_y_shareholders_equity_growth_per_share, ten_y_dividend_per_share_growth_per_share,
                    five_y_dividend_per_share_growth_per_share, three_y_dividend_per_share_growth_per_share,
                    ebitda_growth, growth_capital_expenditure, ten_y_bottom_line_net_income_growth_per_share,
                    five_y_bottom_line_net_income_growth_per_share, three_y_bottom_line_net_income_growth_per_share
                ) VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
            """, (
                data.get("symbol"), data.get("date"), data.get("fiscal_year"), data.get("period"), data.get("reported_currency"),
                data.get("revenue_growth"), data.get("gross_profit_growth"), data.get("ebit_growth"), data.get("operating_income_growth"),
                data.get("net_income_growth"), data.get("eps_growth"), data.get("eps_diluted_growth"), data.get("weighted_average_shares_growth"),
                data.get("weighted_average_shares_diluted_growth"), data.get("dividends_per_share_growth"), data.get("operating_cash_flow_growth"),
                data.get("receivables_growth"), data.get("inventory_growth"), data.get("asset_growth"), data.get("book_value_per_share_growth"),
                data.get("debt_growth"), data.get("rd_expense_growth"), data.get("sga_expenses_growth"), data.get("free_cash_flow_growth"),
                data.get("ten_y_revenue_growth_per_share"), data.get("five_y_revenue_growth_per_share"), data.get("three_y_revenue_growth_per_share"),
                data.get("ten_y_operating_cf_growth_per_share"), data.get("five_y_operating_cf_growth_per_share"), data.get("three_y_operating_cf_growth_per_share"),
                data.get("ten_y_net_income_growth_per_share"), data.get("five_y_net_income_growth_per_share"), data.get("three_y_net_income_growth_per_share"),
                data.get("ten_y_shareholders_equity_growth_per_share"), data.get("five_y_shareholders_equity_growth_per_share"),
                data.get("three_y_shareholders_equity_growth_per_share"), data.get("ten_y_dividend_per_share_growth_per_share"),
                data.get("five_y_dividend_per_share_growth_per_share"), data.get("three_y_dividend_per_share_growth_per_share"),
                data.get("ebitda_growth"), data.get("growth_capital_expenditure"),
                data.get("ten_y_bottom_line_net_income_growth_per_share"), data.get("five_y_bottom_line_net_income_growth_per_share"),
                data.get("three_y_bottom_line_net_income_growth_per_share")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing financial statement growth for {data.get('symbol')} on {data.get('date')}: {e}")

    def store_income_statement_growth(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO income_statement_growth (
                    symbol, date, fiscal_year, period, reported_currency,
                    revenue, cost_of_revenue, gross_profit, gross_profit_ratio,
                    research_and_development_expenses, general_and_administrative_expenses,
                    selling_and_marketing_expenses, other_expenses, operating_expenses,
                    cost_and_expenses, interest_income, interest_expense,
                    depreciation_and_amortization, ebitda, operating_income,
                    income_before_tax, income_tax_expense, net_income,
                    eps, eps_diluted, weighted_average_shs_out,
                    weighted_average_shs_out_dil, ebit, non_operating_income_excluding_interest,
                    net_interest_income, total_other_income_expenses_net,
                    net_income_from_continuing_operations, other_adjustments_to_net_income,
                    net_income_deductions
                ) VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
            """, (
                data.get("symbol"), data.get("date"), data.get("fiscal_year"), data.get("period"), data.get("reported_currency"),
                data.get("revenue"), data.get("cost_of_revenue"), data.get("gross_profit"), data.get("gross_profit_ratio"),
                data.get("research_and_development_expenses"), data.get("general_and_administrative_expenses"),
                data.get("selling_and_marketing_expenses"), data.get("other_expenses"), data.get("operating_expenses"),
                data.get("cost_and_expenses"), data.get("interest_income"), data.get("interest_expense"),
                data.get("depreciation_and_amortization"), data.get("ebitda"), data.get("operating_income"),
                data.get("income_before_tax"), data.get("income_tax_expense"), data.get("net_income"),
                data.get("eps"), data.get("eps_diluted"), data.get("weighted_average_shs_out"),
                data.get("weighted_average_shs_out_dil"), data.get("ebit"), data.get("non_operating_income_excluding_interest"),
                data.get("net_interest_income"), data.get("total_other_income_expenses_net"),
                data.get("net_income_from_continuing_operations"), data.get("other_adjustments_to_net_income"),
                data.get("net_income_deductions")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing income statement growth for {data.get('symbol')} on {data.get('date')}: {e}")
