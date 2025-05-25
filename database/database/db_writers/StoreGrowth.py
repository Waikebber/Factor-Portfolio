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
                    growth_cash_and_cash_equivalents, growth_short_term_investments, growth_cash_and_short_term_investments,
                    growth_net_receivables, growth_inventory, growth_other_current_assets, growth_total_current_assets,
                    growth_property_plant_equipment_net, growth_goodwill, growth_intangible_assets, growth_goodwill_and_intangible_assets,
                    growth_long_term_investments, growth_tax_assets, growth_other_non_current_assets, growth_total_non_current_assets,
                    growth_other_assets, growth_total_assets, growth_account_payables, growth_short_term_debt, growth_tax_payables,
                    growth_deferred_revenue, growth_other_current_liabilities, growth_total_current_liabilities, growth_long_term_debt,
                    growth_deferred_revenue_non_current, growth_deferred_tax_liabilities_non_current, growth_other_non_current_liabilities,
                    growth_total_non_current_liabilities, growth_other_liabilities, growth_total_liabilities, growth_preferred_stock,
                    growth_common_stock, growth_retained_earnings, growth_accumulated_other_comprehensive_income_loss,
                    growth_other_total_stockholders_equity, growth_total_stockholders_equity, growth_minority_interest, growth_total_equity,
                    growth_total_liabilities_and_stockholders_equity, growth_total_investments, growth_total_debt, growth_net_debt,
                    growth_accounts_receivables, growth_other_receivables, growth_prepaids, growth_total_payables, growth_other_payables,
                    growth_accrued_expenses, growth_capital_lease_obligations_current, growth_additional_paid_in_capital,
                    growth_treasury_stock
                ) VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
            """, (
                data.get("symbol"), data.get("date"), data.get("fiscal_year"), data.get("period"), data.get("reported_currency"),
                data.get("growth_cash_and_cash_equivalents"), data.get("growth_short_term_investments"), data.get("growth_cash_and_short_term_investments"),
                data.get("growth_net_receivables"), data.get("growth_inventory"), data.get("growth_other_current_assets"), data.get("growth_total_current_assets"),
                data.get("growth_property_plant_equipment_net"), data.get("growth_goodwill"), data.get("growth_intangible_assets"), data.get("growth_goodwill_and_intangible_assets"),
                data.get("growth_long_term_investments"), data.get("growth_tax_assets"), data.get("growth_other_non_current_assets"), data.get("growth_total_non_current_assets"),
                data.get("growth_other_assets"), data.get("growth_total_assets"), data.get("growth_account_payables"), data.get("growth_short_term_debt"), data.get("growth_tax_payables"),
                data.get("growth_deferred_revenue"), data.get("growth_other_current_liabilities"), data.get("growth_total_current_liabilities"), data.get("growth_long_term_debt"),
                data.get("growth_deferred_revenue_non_current"), data.get("growth_deferred_tax_liabilities_non_current"), data.get("growth_other_non_current_liabilities"),
                data.get("growth_total_non_current_liabilities"), data.get("growth_other_liabilities"), data.get("growth_total_liabilities"), data.get("growth_preferred_stock"),
                data.get("growth_common_stock"), data.get("growth_retained_earnings"), data.get("growth_accumulated_other_comprehensive_income_loss"),
                data.get("growth_other_total_stockholders_equity"), data.get("growth_total_stockholders_equity"), data.get("growth_minority_interest"), data.get("growth_total_equity"),
                data.get("growth_total_liabilities_and_stockholders_equity"), data.get("growth_total_investments"), data.get("growth_total_debt"), data.get("growth_net_debt"),
                data.get("growth_accounts_receivables"), data.get("growth_other_receivables"), data.get("growth_prepaids"), data.get("growth_total_payables"), data.get("growth_other_payables"),
                data.get("growth_accrued_expenses"), data.get("growth_capital_lease_obligations_current"), data.get("growth_additional_paid_in_capital"),
                data.get("growth_treasury_stock")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing balance sheet growth for {data.get('symbol')} on {data.get('date')}: {e}")

    def store_cashflow_statement_growth(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO cashflow_statement_growth (
                    symbol, date, fiscal_year, period, reported_currency,
                    growth_net_income, growth_depreciation_and_amortization, growth_deferred_income_tax,
                    growth_stock_based_compensation, growth_change_in_working_capital, growth_accounts_receivables,
                    growth_inventory, growth_accounts_payables, growth_other_working_capital, growth_other_non_cash_items,
                    growth_net_cash_provided_by_operating_activities, growth_investments_in_property_plant_and_equipment,
                    growth_acquisitions_net, growth_purchases_of_investments, growth_sales_maturities_of_investments,
                    growth_other_investing_activities, growth_net_cash_used_for_investing_activities, growth_debt_repayment,
                    growth_common_stock_issued, growth_common_stock_repurchased, growth_dividends_paid,
                    growth_other_financing_activities, growth_net_cash_used_provided_by_financing_activities,
                    growth_effect_of_forex_changes_on_cash, growth_net_change_in_cash, growth_cash_at_end_of_period,
                    growth_cash_at_beginning_of_period, growth_operating_cash_flow, growth_capital_expenditure,
                    growth_free_cash_flow, growth_net_debt_issuance, growth_long_term_net_debt_issuance,
                    growth_short_term_net_debt_issuance, growth_net_stock_issuance, growth_preferred_dividends_paid,
                    growth_income_taxes_paid, growth_interest_paid
                ) VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
            """, (
                data.get("symbol"), data.get("date"), data.get("fiscal_year"), data.get("period"), data.get("reported_currency"),
                data.get("growth_net_income"), data.get("growth_depreciation_and_amortization"), data.get("growth_deferred_income_tax"),
                data.get("growth_stock_based_compensation"), data.get("growth_change_in_working_capital"), data.get("growth_accounts_receivables"),
                data.get("growth_inventory"), data.get("growth_accounts_payables"), data.get("growth_other_working_capital"),
                data.get("growth_other_non_cash_items"), data.get("growth_net_cash_provided_by_operating_activites"),
                data.get("growth_investments_in_property_plant_and_equipment"), data.get("growth_acquisitions_net"),
                data.get("growth_purchases_of_investments"), data.get("growth_sales_maturities_of_investments"),
                data.get("growth_other_investing_activities"), data.get("growth_net_cash_used_for_investing_activities"),
                data.get("growth_debt_repayment"), data.get("growth_common_stock_issued"), data.get("growth_common_stock_repurchased"),
                data.get("growth_dividends_paid"), data.get("growth_other_financing_activities"),
                data.get("growth_net_cash_used_provided_by_financing_activities"), data.get("growth_effect_of_forex_changes_on_cash"),
                data.get("growth_net_change_in_cash"), data.get("growth_cash_at_end_of_period"), data.get("growth_cash_at_beginning_of_period"),
                data.get("growth_operating_cash_flow"), data.get("growth_capital_expenditure"), data.get("growth_free_cash_flow"),
                data.get("growth_net_debt_issuance"), data.get("growth_long_term_net_debt_issuance"),
                data.get("growth_short_term_net_debt_issuance"), data.get("growth_net_stock_issuance"),
                data.get("growth_preferred_dividends_paid"), data.get("growth_income_taxes_paid"), data.get("growth_interest_paid")
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
                    growth_revenue, growth_cost_of_revenue, growth_gross_profit, growth_gross_profit_ratio,
                    growth_research_and_development_expenses, growth_general_and_administrative_expenses,
                    growth_selling_and_marketing_expenses, growth_other_expenses, growth_operating_expenses,
                    growth_cost_and_expenses, growth_interest_income, growth_interest_expense,
                    growth_depreciation_and_amortization, growth_ebitda, growth_operating_income,
                    growth_income_before_tax, growth_income_tax_expense, growth_net_income,
                    growth_eps, growth_eps_diluted, growth_weighted_average_shs_out,
                    growth_weighted_average_shs_out_dil, growth_ebit, growth_non_operating_income_excluding_interest,
                    growth_net_interest_income, growth_total_other_income_expenses_net,
                    growth_net_income_from_continuing_operations, growth_other_adjustments_to_net_income,
                    growth_net_income_deductions
                ) VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
            """, (
                data.get("symbol"), data.get("date"), data.get("fiscal_year"), data.get("period"), data.get("reported_currency"),
                data.get("growth_revenue"), data.get("growth_cost_of_revenue"), data.get("growth_gross_profit"), data.get("growth_gross_profit_ratio"),
                data.get("growth_research_and_development_expenses"), data.get("growth_general_and_administrative_expenses"),
                data.get("growth_selling_and_marketing_expenses"), data.get("growth_other_expenses"), data.get("growth_operating_expenses"),
                data.get("growth_cost_and_expenses"), data.get("growth_interest_income"), data.get("growth_interest_expense"),
                data.get("growth_depreciation_and_amortization"), data.get("growth_ebitda"), data.get("growth_operating_income"),
                data.get("growth_income_before_tax"), data.get("growth_income_tax_expense"), data.get("growth_net_income"),
                data.get("growth_eps"), data.get("growth_eps_diluted"), data.get("growth_weighted_average_shs_out"),
                data.get("growth_weighted_average_shs_out_dil"), data.get("growth_ebit"), data.get("growth_non_operating_income_excluding_interest"),
                data.get("growth_net_interest_income"), data.get("growth_total_other_income_expenses_net"),
                data.get("growth_net_income_from_continuing_operations"), data.get("growth_other_adjustments_to_net_income"),
                data.get("growth_net_income_deductions")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing income statement growth for {data.get('symbol')} on {data.get('date')}: {e}")
