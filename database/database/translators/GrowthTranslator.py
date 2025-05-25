from typing import Dict, Any, List
from .utils import safe_float, safe_int

class GrowthTranslator:
    @staticmethod
    def translate_financial_statement_growth(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates financial statement growth data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw financial statement growth data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated financial statement growth data in the database schema format
        """
        if not data:
            return []
        
        translated_growth = []
        for growth in data:
            translated = {
                "symbol": growth.get('symbol'),
                "date": growth.get('date'),
                "fiscal_year": growth.get('fiscalYear'),
                "period": growth.get('period'),
                "reported_currency": growth.get('reportedCurrency'),
                "revenue_growth": safe_float(growth.get('revenueGrowth')),
                "gross_profit_growth": safe_float(growth.get('grossProfitGrowth')),
                "ebit_growth": safe_float(growth.get('ebitgrowth')),
                "operating_income_growth": safe_float(growth.get('operatingIncomeGrowth')),
                "net_income_growth": safe_float(growth.get('netIncomeGrowth')),
                "eps_growth": safe_float(growth.get('epsgrowth')),
                "eps_diluted_growth": safe_float(growth.get('epsdilutedGrowth')),
                "weighted_average_shares_growth": safe_float(growth.get('weightedAverageSharesGrowth')),
                "weighted_average_shares_diluted_growth": safe_float(growth.get('weightedAverageSharesDilutedGrowth')),
                "dividends_per_share_growth": safe_float(growth.get('dividendsPerShareGrowth')),
                "operating_cash_flow_growth": safe_float(growth.get('operatingCashFlowGrowth')),
                "receivables_growth": safe_float(growth.get('receivablesGrowth')),
                "inventory_growth": safe_float(growth.get('inventoryGrowth')),
                "asset_growth": safe_float(growth.get('assetGrowth')),
                "book_value_per_share_growth": safe_float(growth.get('bookValueperShareGrowth')),
                "debt_growth": safe_float(growth.get('debtGrowth')),
                "rd_expense_growth": safe_float(growth.get('rdexpenseGrowth')),
                "sga_expenses_growth": safe_float(growth.get('sgaexpensesGrowth')),
                "free_cash_flow_growth": safe_float(growth.get('freeCashFlowGrowth')),
                "ten_y_revenue_growth_per_share": safe_float(growth.get('tenYRevenueGrowthPerShare')),
                "five_y_revenue_growth_per_share": safe_float(growth.get('fiveYRevenueGrowthPerShare')),
                "three_y_revenue_growth_per_share": safe_float(growth.get('threeYRevenueGrowthPerShare')),
                "ten_y_operating_cf_growth_per_share": safe_float(growth.get('tenYOperatingCFGrowthPerShare')),
                "five_y_operating_cf_growth_per_share": safe_float(growth.get('fiveYOperatingCFGrowthPerShare')),
                "three_y_operating_cf_growth_per_share": safe_float(growth.get('threeYOperatingCFGrowthPerShare')),
                "ten_y_net_income_growth_per_share": safe_float(growth.get('tenYNetIncomeGrowthPerShare')),
                "five_y_net_income_growth_per_share": safe_float(growth.get('fiveYNetIncomeGrowthPerShare')),
                "three_y_net_income_growth_per_share": safe_float(growth.get('threeYNetIncomeGrowthPerShare')),
                "ten_y_shareholders_equity_growth_per_share": safe_float(growth.get('tenYShareholdersEquityGrowthPerShare')),
                "five_y_shareholders_equity_growth_per_share": safe_float(growth.get('fiveYShareholdersEquityGrowthPerShare')),
                "three_y_shareholders_equity_growth_per_share": safe_float(growth.get('threeYShareholdersEquityGrowthPerShare')),
                "ten_y_dividend_per_share_growth_per_share": safe_float(growth.get('tenYDividendperShareGrowthPerShare')),
                "five_y_dividend_per_share_growth_per_share": safe_float(growth.get('fiveYDividendperShareGrowthPerShare')),
                "three_y_dividend_per_share_growth_per_share": safe_float(growth.get('threeYDividendperShareGrowthPerShare')),
                "ebitda_growth": safe_float(growth.get('ebitdaGrowth')),
                "growth_capital_expenditure": safe_float(growth.get('growthCapitalExpenditure')),
                "ten_y_bottom_line_net_income_growth_per_share": safe_float(growth.get('tenYBottomLineNetIncomeGrowthPerShare')),
                "five_y_bottom_line_net_income_growth_per_share": safe_float(growth.get('fiveYBottomLineNetIncomeGrowthPerShare')),
                "three_y_bottom_line_net_income_growth_per_share": safe_float(growth.get('threeYBottomLineNetIncomeGrowthPerShare'))
            }
            translated_growth.append(translated)
        
        return translated_growth

    @staticmethod
    def translate_cashflow_statement_growth(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates cashflow statement growth data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw cashflow statement growth data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated cashflow statement growth data in the database schema format
        """
        if not data:
            return []
        translated_growth = []
        for growth in data:
            translated = {
                "symbol": growth.get('symbol'),
                "date": growth.get('date'),
                "fiscal_year": growth.get('fiscalYear'),
                "period": growth.get('period'),
                "reported_currency": growth.get('reportedCurrency'),
                "growth_net_income": safe_float(growth.get('growthNetIncome')),
                "growth_depreciation_and_amortization": safe_float(growth.get('growthDepreciationAndAmortization')),
                "growth_deferred_income_tax": safe_float(growth.get('growthDeferredIncomeTax')),
                "growth_stock_based_compensation": safe_float(growth.get('growthStockBasedCompensation')),
                "growth_change_in_working_capital": safe_float(growth.get('growthChangeInWorkingCapital')),
                "growth_accounts_receivables": safe_float(growth.get('growthAccountsReceivables')),
                "growth_inventory": safe_float(growth.get('growthInventory')),
                "growth_accounts_payables": safe_float(growth.get('growthAccountsPayables')),
                "growth_other_working_capital": safe_float(growth.get('growthOtherWorkingCapital')),
                "growth_other_non_cash_items": safe_float(growth.get('growthOtherNonCashItems')),
                "growth_net_cash_provided_by_operating_activites": safe_float(growth.get('growthNetCashProvidedByOperatingActivites')),
                "growth_investments_in_property_plant_and_equipment": safe_float(growth.get('growthInvestmentsInPropertyPlantAndEquipment')),
                "growth_acquisitions_net": safe_float(growth.get('growthAcquisitionsNet')),
                "growth_purchases_of_investments": safe_float(growth.get('growthPurchasesOfInvestments')),
                "growth_sales_maturities_of_investments": safe_float(growth.get('growthSalesMaturitiesOfInvestments')),
                "growth_other_investing_activites": safe_float(growth.get('growthOtherInvestingActivites')),
                "growth_net_cash_used_for_investing_activites": safe_float(growth.get('growthNetCashUsedForInvestingActivites')),
                "growth_debt_repayment": safe_float(growth.get('growthDebtRepayment')),
                "growth_common_stock_issued": safe_float(growth.get('growthCommonStockIssued')),
                "growth_common_stock_repurchased": safe_float(growth.get('growthCommonStockRepurchased')),
                "growth_dividends_paid": safe_float(growth.get('growthDividendsPaid')),
                "growth_other_financing_activites": safe_float(growth.get('growthOtherFinancingActivites')),
                "growth_net_cash_used_provided_by_financing_activities": safe_float(growth.get('growthNetCashUsedProvidedByFinancingActivities')),
                "growth_effect_of_forex_changes_on_cash": safe_float(growth.get('growthEffectOfForexChangesOnCash')),
                "growth_net_change_in_cash": safe_float(growth.get('growthNetChangeInCash')),
                "growth_cash_at_end_of_period": safe_float(growth.get('growthCashAtEndOfPeriod')),
                "growth_cash_at_beginning_of_period": safe_float(growth.get('growthCashAtBeginningOfPeriod')),
                "growth_operating_cash_flow": safe_float(growth.get('growthOperatingCashFlow')),
                "growth_capital_expenditure": safe_float(growth.get('growthCapitalExpenditure')),
                "growth_free_cash_flow": safe_float(growth.get('growthFreeCashFlow')),
                "growth_net_debt_issuance": safe_float(growth.get('growthNetDebtIssuance')),
                "growth_long_term_net_debt_issuance": safe_float(growth.get('growthLongTermNetDebtIssuance')),
                "growth_short_term_net_debt_issuance": safe_float(growth.get('growthShortTermNetDebtIssuance')),
                "growth_net_stock_issuance": safe_float(growth.get('growthNetStockIssuance')),
                "growth_preferred_dividends_paid": safe_float(growth.get('growthPreferredDividendsPaid')),
                "growth_income_taxes_paid": safe_float(growth.get('growthIncomeTaxesPaid')),
                "growth_interest_paid": safe_float(growth.get('growthInterestPaid'))
            }
            translated_growth.append(translated)
        
        return translated_growth

    @staticmethod
    def translate_balance_sheet_growth(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates balance sheet growth data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw balance sheet growth data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated balance sheet growth data in the database schema format
        """
        if not data:
            return []
        translated_growth = []
        for growth in data:
            translated = {
                'symbol': growth.get('symbol'),
                'date': growth.get('date'),
                'fiscal_year': growth.get('fiscalYear'),
                'period': growth.get('period'),
                'reported_currency': growth.get('reportedCurrency'),
                'growth_cash_and_cash_equivalents': safe_float(growth.get('growthCashAndCashEquivalents')),
                'growth_short_term_investments': safe_float(growth.get('growthShortTermInvestments')),
                'growth_cash_and_short_term_investments': safe_float(growth.get('growthCashAndShortTermInvestments')),
                'growth_net_receivables': safe_float(growth.get('growthNetReceivables')),
                'growth_inventory': safe_float(growth.get('growthInventory')),
                'growth_other_current_assets': safe_float(growth.get('growthOtherCurrentAssets')),
                'growth_total_current_assets': safe_float(growth.get('growthTotalCurrentAssets')),
                'growth_property_plant_equipment_net': safe_float(growth.get('growthPropertyPlantEquipmentNet')),
                'growth_goodwill': safe_float(growth.get('growthGoodwill')),
                'growth_intangible_assets': safe_float(growth.get('growthIntangibleAssets')),
                'growth_goodwill_and_intangible_assets': safe_float(growth.get('growthGoodwillAndIntangibleAssets')),
                'growth_long_term_investments': safe_float(growth.get('growthLongTermInvestments')),
                'growth_tax_assets': safe_float(growth.get('growthTaxAssets')),
                'growth_other_non_current_assets': safe_float(growth.get('growthOtherNonCurrentAssets')),
                'growth_total_non_current_assets': safe_float(growth.get('growthTotalNonCurrentAssets')),
                'growth_other_assets': safe_float(growth.get('growthOtherAssets')),
                'growth_total_assets': safe_float(growth.get('growthTotalAssets')),
                'growth_account_payables': safe_float(growth.get('growthAccountPayables')),
                'growth_short_term_debt': safe_float(growth.get('growthShortTermDebt')),
                'growth_tax_payables': safe_float(growth.get('growthTaxPayables')),
                'growth_deferred_revenue': safe_float(growth.get('growthDeferredRevenue')),
                'growth_other_current_liabilities': safe_float(growth.get('growthOtherCurrentLiabilities')),
                'growth_total_current_liabilities': safe_float(growth.get('growthTotalCurrentLiabilities')),
                'growth_long_term_debt': safe_float(growth.get('growthLongTermDebt')),
                'growth_deferred_revenue_non_current': safe_float(growth.get('growthDeferredRevenueNonCurrent')),
                'growth_deferred_tax_liabilities_non_current': safe_float(growth.get('growthDeferredTaxLiabilitiesNonCurrent')),
                'growth_other_non_current_liabilities': safe_float(growth.get('growthOtherNonCurrentLiabilities')),
                'growth_total_non_current_liabilities': safe_float(growth.get('growthTotalNonCurrentLiabilities')),
                'growth_other_liabilities': safe_float(growth.get('growthOtherLiabilities')),
                'growth_total_liabilities': safe_float(growth.get('growthTotalLiabilities')),
                'growth_preferred_stock': safe_float(growth.get('growthPreferredStock')),
                'growth_common_stock': safe_float(growth.get('growthCommonStock')),
                'growth_retained_earnings': safe_float(growth.get('growthRetainedEarnings')),
                'growth_accumulated_other_comprehensive_income_loss': safe_float(growth.get('growthAccumulatedOtherComprehensiveIncomeLoss')),
                'growth_other_total_stockholders_equity': safe_float(growth.get('growthOthertotalStockholdersEquity')),
                'growth_total_stockholders_equity': safe_float(growth.get('growthTotalStockholdersEquity')),
                'growth_minority_interest': safe_float(growth.get('growthMinorityInterest')),
                'growth_total_equity': safe_float(growth.get('growthTotalEquity')),
                'growth_total_liabilities_and_stockholders_equity': safe_float(growth.get('growthTotalLiabilitiesAndStockholdersEquity')),
                'growth_total_investments': safe_float(growth.get('growthTotalInvestments')),
                'growth_total_debt': safe_float(growth.get('growthTotalDebt')),
                'growth_net_debt': safe_float(growth.get('growthNetDebt')),
                'growth_accounts_receivables': safe_float(growth.get('growthAccountsReceivables')),
                'growth_other_receivables': safe_float(growth.get('growthOtherReceivables')),
                'growth_prepaids': safe_float(growth.get('growthPrepaids')),
                'growth_total_payables': safe_float(growth.get('growthTotalPayables')),
                'growth_other_payables': safe_float(growth.get('growthOtherPayables')),
                'growth_accrued_expenses': safe_float(growth.get('growthAccruedExpenses')),
                'growth_capital_lease_obligations_current': safe_float(growth.get('growthCapitalLeaseObligationsCurrent')),
                'growth_additional_paid_in_capital': safe_float(growth.get('growthAdditionalPaidInCapital')),
                'growth_treasury_stock': safe_float(growth.get('growthTreasuryStock'))
            }
            translated_growth.append(translated)
        return translated_growth

    @staticmethod
    def translate_income_statement_growth(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates income statement growth data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw income statement growth data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated income statement growth data in the database schema format
        """
        if not data:
            return []
        
        translated_growth = []
        for growth in data:
            translated = {
                "symbol": growth.get('symbol'),
                "date": growth.get('date'),
                "fiscal_year": growth.get('fiscalYear'),
                "period": growth.get('period'),
                "reported_currency": growth.get('reportedCurrency'),
                "growth_revenue": safe_float(growth.get('growthRevenue')),
                "growth_cost_of_revenue": safe_float(growth.get('growthCostOfRevenue')),
                "growth_gross_profit": safe_float(growth.get('growthGrossProfit')),
                "growth_gross_profit_ratio": safe_float(growth.get('growthGrossProfitRatio')),
                "growth_research_and_development_expenses": safe_float(growth.get('growthResearchAndDevelopmentExpenses')),
                "growth_general_and_administrative_expenses": safe_float(growth.get('growthGeneralAndAdministrativeExpenses')),
                "growth_selling_and_marketing_expenses": safe_float(growth.get('growthSellingAndMarketingExpenses')),
                "growth_other_expenses": safe_float(growth.get('growthOtherExpenses')),
                "growth_operating_expenses": safe_float(growth.get('growthOperatingExpenses')),
                "growth_cost_and_expenses": safe_float(growth.get('growthCostAndExpenses')),
                "growth_interest_income": safe_float(growth.get('growthInterestIncome')),
                "growth_interest_expense": safe_float(growth.get('growthInterestExpense')),
                "growth_depreciation_and_amortization": safe_float(growth.get('growthDepreciationAndAmortization')),
                "growth_ebitda": safe_float(growth.get('growthEBITDA')),
                "growth_operating_income": safe_float(growth.get('growthOperatingIncome')),
                "growth_income_before_tax": safe_float(growth.get('growthIncomeBeforeTax')),
                "growth_income_tax_expense": safe_float(growth.get('growthIncomeTaxExpense')),
                "growth_net_income": safe_float(growth.get('growthNetIncome')),
                "growth_eps": safe_float(growth.get('growthEPS')),
                "growth_eps_diluted": safe_float(growth.get('growthEPSDiluted')),
                "growth_weighted_average_shs_out": safe_float(growth.get('growthWeightedAverageShsOut')),
                "growth_weighted_average_shs_out_diluted": safe_float(growth.get('growthWeightedAverageShsOutDil')),
                "growth_ebit": safe_float(growth.get('growthEBIT')),
                "growth_non_operating_income_excluding_interest": safe_float(growth.get('growthNonOperatingIncomeExcludingInterest')),
                "growth_net_interest_income": safe_float(growth.get('growthNetInterestIncome')),
                "growth_total_other_income_expenses_net": safe_float(growth.get('growthTotalOtherIncomeExpensesNet')),
                "growth_net_income_from_continuing_operations": safe_float(growth.get('growthNetIncomeFromContinuingOperations')),
                "growth_other_adjustments_to_net_income": safe_float(growth.get('growthOtherAdjustmentsToNetIncome')),
                "growth_net_income_deductions": safe_float(growth.get('growthNetIncomeDeductions'))
            }
            translated_growth.append(translated)
        
        return translated_growth 