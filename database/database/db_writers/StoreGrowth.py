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
                    growth_othertotal_stockholders_equity, growth_total_stockholders_equity, growth_minority_interest, growth_total_equity,
                    growth_total_liabilities_and_stockholders_equity, growth_total_investments, growth_total_debt, growth_net_debt,
                    growth_accounts_receivables, growth_other_receivables, growth_prepaids, growth_total_payables, growth_other_payables,
                    growth_accrued_expenses, growth_capital_lease_obligations_current, growth_additional_paid_in_capital,
                    growth_treasury_stock, last_updated
                ) VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now')
                )
            """, (
                data.get("symbol"), data.get("date"), data.get("fiscalYear"), data.get("period"), data.get("reportedCurrency"),
                data.get("growthCashAndCashEquivalents"), data.get("growthShortTermInvestments"), data.get("growthCashAndShortTermInvestments"),
                data.get("growthNetReceivables"), data.get("growthInventory"), data.get("growthOtherCurrentAssets"), data.get("growthTotalCurrentAssets"),
                data.get("growthPropertyPlantEquipmentNet"), data.get("growthGoodwill"), data.get("growthIntangibleAssets"), data.get("growthGoodwillAndIntangibleAssets"),
                data.get("growthLongTermInvestments"), data.get("growthTaxAssets"), data.get("growthOtherNonCurrentAssets"), data.get("growthTotalNonCurrentAssets"),
                data.get("growthOtherAssets"), data.get("growthTotalAssets"), data.get("growthAccountPayables"), data.get("growthShortTermDebt"), data.get("growthTaxPayables"),
                data.get("growthDeferredRevenue"), data.get("growthOtherCurrentLiabilities"), data.get("growthTotalCurrentLiabilities"), data.get("growthLongTermDebt"),
                data.get("growthDeferredRevenueNonCurrent"), data.get("growthDeferredTaxLiabilitiesNonCurrent"), data.get("growthOtherNonCurrentLiabilities"),
                data.get("growthTotalNonCurrentLiabilities"), data.get("growthOtherLiabilities"), data.get("growthTotalLiabilities"), data.get("growthPreferredStock"),
                data.get("growthCommonStock"), data.get("growthRetainedEarnings"), data.get("growthAccumulatedOtherComprehensiveIncomeLoss"),
                data.get("growthOthertotalStockholdersEquity"), data.get("growthTotalStockholdersEquity"), data.get("growthMinorityInterest"), data.get("growthTotalEquity"),
                data.get("growthTotalLiabilitiesAndStockholdersEquity"), data.get("growthTotalInvestments"), data.get("growthTotalDebt"), data.get("growthNetDebt"),
                data.get("growthAccountsReceivables"), data.get("growthOtherReceivables"), data.get("growthPrepaids"), data.get("growthTotalPayables"), data.get("growthOtherPayables"),
                data.get("growthAccruedExpenses"), data.get("growthCapitalLeaseObligationsCurrent"), data.get("growthAdditionalPaidInCapital"),
                data.get("growthTreasuryStock")
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
                    growth_income_taxes_paid, growth_interest_paid, last_updated
                ) VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now')
                )
            """, (
                data.get("symbol"), data.get("date"), data.get("fiscalYear"), data.get("period"), data.get("reportedCurrency"),
                data.get("growthNetIncome"), data.get("growthDepreciationAndAmortization"), data.get("growthDeferredIncomeTax"),
                data.get("growthStockBasedCompensation"), data.get("growthChangeInWorkingCapital"), data.get("growthAccountsReceivables"),
                data.get("growthInventory"), data.get("growthAccountsPayables"), data.get("growthOtherWorkingCapital"),
                data.get("growthOtherNonCashItems"), data.get("growthNetCashProvidedByOperatingActivites"),
                data.get("growthInvestmentsInPropertyPlantAndEquipment"), data.get("growthAcquisitionsNet"),
                data.get("growthPurchasesOfInvestments"), data.get("growthSalesMaturitiesOfInvestments"),
                data.get("growthOtherInvestingActivites"), data.get("growthNetCashUsedForInvestingActivites"),
                data.get("growthDebtRepayment"), data.get("growthCommonStockIssued"), data.get("growthCommonStockRepurchased"),
                data.get("growthDividendsPaid"), data.get("growthOtherFinancingActivites"),
                data.get("growthNetCashUsedProvidedByFinancingActivities"), data.get("growthEffectOfForexChangesOnCash"),
                data.get("growthNetChangeInCash"), data.get("growthCashAtEndOfPeriod"), data.get("growthCashAtBeginningOfPeriod"),
                data.get("growthOperatingCashFlow"), data.get("growthCapitalExpenditure"), data.get("growthFreeCashFlow"),
                data.get("growthNetDebtIssuance"), data.get("growthLongTermNetDebtIssuance"),
                data.get("growthShortTermNetDebtIssuance"), data.get("growthNetStockIssuance"),
                data.get("growthPreferredDividendsPaid"), data.get("growthIncomeTaxesPaid"), data.get("growthInterestPaid")
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
                    five_y_bottom_line_net_income_growth_per_share, three_y_bottom_line_net_income_growth_per_share,
                    last_updated
                ) VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now')
                )
            """, (
                data.get("symbol"), data.get("date"), data.get("fiscalYear"), data.get("period"), data.get("reportedCurrency"),
                data.get("revenueGrowth"), data.get("grossProfitGrowth"), data.get("ebitgrowth"), data.get("operatingIncomeGrowth"),
                data.get("netIncomeGrowth"), data.get("epsgrowth"), data.get("epsdilutedGrowth"), data.get("weightedAverageSharesGrowth"),
                data.get("weightedAverageSharesDilutedGrowth"), data.get("dividendsPerShareGrowth"), data.get("operatingCashFlowGrowth"),
                data.get("receivablesGrowth"), data.get("inventoryGrowth"), data.get("assetGrowth"), data.get("bookValueperShareGrowth"),
                data.get("debtGrowth"), data.get("rdexpenseGrowth"), data.get("sgaexpensesGrowth"), data.get("freeCashFlowGrowth"),
                data.get("tenYRevenueGrowthPerShare"), data.get("fiveYRevenueGrowthPerShare"), data.get("threeYRevenueGrowthPerShare"),
                data.get("tenYOperatingCFGrowthPerShare"), data.get("fiveYOperatingCFGrowthPerShare"), data.get("threeYOperatingCFGrowthPerShare"),
                data.get("tenYNetIncomeGrowthPerShare"), data.get("fiveYNetIncomeGrowthPerShare"), data.get("threeYNetIncomeGrowthPerShare"),
                data.get("tenYShareholdersEquityGrowthPerShare"), data.get("fiveYShareholdersEquityGrowthPerShare"),
                data.get("threeYShareholdersEquityGrowthPerShare"), data.get("tenYDividendperShareGrowthPerShare"),
                data.get("fiveYDividendperShareGrowthPerShare"), data.get("threeYDividendperShareGrowthPerShare"),
                data.get("ebitdaGrowth"), data.get("growthCapitalExpenditure"),
                data.get("tenYBottomLineNetIncomeGrowthPerShare"), data.get("fiveYBottomLineNetIncomeGrowthPerShare"),
                data.get("threeYBottomLineNetIncomeGrowthPerShare")
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
                    growth_net_income_deductions, last_updated
                ) VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now')
                )
            """, (
                data.get("symbol"), data.get("date"), data.get("fiscalYear"), data.get("period"), data.get("reportedCurrency"),
                data.get("growthRevenue"), data.get("growthCostOfRevenue"), data.get("growthGrossProfit"), data.get("growthGrossProfitRatio"),
                data.get("growthResearchAndDevelopmentExpenses"), data.get("growthGeneralAndAdministrativeExpenses"),
                data.get("growthSellingAndMarketingExpenses"), data.get("growthOtherExpenses"), data.get("growthOperatingExpenses"),
                data.get("growthCostAndExpenses"), data.get("growthInterestIncome"), data.get("growthInterestExpense"),
                data.get("growthDepreciationAndAmortization"), data.get("growthEBITDA"), data.get("growthOperatingIncome"),
                data.get("growthIncomeBeforeTax"), data.get("growthIncomeTaxExpense"), data.get("growthNetIncome"),
                data.get("growthEPS"), data.get("growthEPSDiluted"), data.get("growthWeightedAverageShsOut"),
                data.get("growthWeightedAverageShsOutDil"), data.get("growthEBIT"), data.get("growthNonOperatingIncomeExcludingInterest"),
                data.get("growthNetInterestIncome"), data.get("growthTotalOtherIncomeExpensesNet"),
                data.get("growthNetIncomeFromContinuingOperations"), data.get("growthOtherAdjustmentsToNetIncome"),
                data.get("growthNetIncomeDeductions")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing income statement growth for {data.get('symbol')} on {data.get('date')}: {e}")
