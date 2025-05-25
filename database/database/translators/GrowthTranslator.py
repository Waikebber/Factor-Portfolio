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
                "net_income": safe_float(growth.get('growthNetIncome')),
                "depreciation_and_amortization": safe_float(growth.get('growthDepreciationAndAmortization')),
                "deferred_income_tax": safe_float(growth.get('growthDeferredIncomeTax')),
                "stock_based_compensation": safe_float(growth.get('growthStockBasedCompensation')),
                "change_in_working_capital": safe_float(growth.get('growthChangeInWorkingCapital')),
                "accounts_receivables": safe_float(growth.get('growthAccountsReceivables')),
                "inventory": safe_float(growth.get('growthInventory')),
                "accounts_payables": safe_float(growth.get('growthAccountsPayables')),
                "other_working_capital": safe_float(growth.get('growthOtherWorkingCapital')),
                "other_non_cash_items": safe_float(growth.get('growthOtherNonCashItems')),
                "net_cash_provided_by_operating_activites": safe_float(growth.get('growthNetCashProvidedByOperatingActivites')),
                "investments_in_property_plant_and_equipment": safe_float(growth.get('growthInvestmentsInPropertyPlantAndEquipment')),
                "acquisitions_net": safe_float(growth.get('growthAcquisitionsNet')),
                "purchases_of_investments": safe_float(growth.get('growthPurchasesOfInvestments')),
                "sales_maturities_of_investments": safe_float(growth.get('growthSalesMaturitiesOfInvestments')),
                "other_investing_activites": safe_float(growth.get('growthOtherInvestingActivites')),
                "net_cash_used_for_investing_activites": safe_float(growth.get('growthNetCashUsedForInvestingActivites')),
                "debt_repayment": safe_float(growth.get('growthDebtRepayment')),
                "common_stock_issued": safe_float(growth.get('growthCommonStockIssued')),
                "common_stock_repurchased": safe_float(growth.get('growthCommonStockRepurchased')),
                "dividends_paid": safe_float(growth.get('growthDividendsPaid')),
                "other_financing_activites": safe_float(growth.get('growthOtherFinancingActivites')),
                "net_cash_used_provided_by_financing_activities": safe_float(growth.get('growthNetCashUsedProvidedByFinancingActivities')),
                "effect_of_forex_changes_on_cash": safe_float(growth.get('growthEffectOfForexChangesOnCash')),
                "net_change_in_cash": safe_float(growth.get('growthNetChangeInCash')),
                "cash_at_end_of_period": safe_float(growth.get('growthCashAtEndOfPeriod')),
                "cash_at_beginning_of_period": safe_float(growth.get('growthCashAtBeginningOfPeriod')),
                "operating_cash_flow": safe_float(growth.get('growthOperatingCashFlow')),
                "capital_expenditure": safe_float(growth.get('growthCapitalExpenditure')),
                "free_cash_flow": safe_float(growth.get('growthFreeCashFlow')),
                "net_debt_issuance": safe_float(growth.get('growthNetDebtIssuance')),
                "long_term_net_debt_issuance": safe_float(growth.get('growthLongTermNetDebtIssuance')),
                "short_term_net_debt_issuance": safe_float(growth.get('growthShortTermNetDebtIssuance')),
                "net_stock_issuance": safe_float(growth.get('growthNetStockIssuance')),
                "preferred_dividends_paid": safe_float(growth.get('growthPreferredDividendsPaid')),
                "income_taxes_paid": safe_float(growth.get('growthIncomeTaxesPaid')),
                "interest_paid": safe_float(growth.get('growthInterestPaid'))
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
                'cash_and_cash_equivalents': safe_float(growth.get('growthCashAndCashEquivalents')),
                'short_term_investments': safe_float(growth.get('growthShortTermInvestments')),
                'cash_and_short_term_investments': safe_float(growth.get('growthCashAndShortTermInvestments')),
                'net_receivables': safe_float(growth.get('growthNetReceivables')),
                'inventory': safe_float(growth.get('growthInventory')),
                'other_current_assets': safe_float(growth.get('growthOtherCurrentAssets')),
                'total_current_assets': safe_float(growth.get('growthTotalCurrentAssets')),
                'property_plant_equipment_net': safe_float(growth.get('growthPropertyPlantEquipmentNet')),
                'goodwill': safe_float(growth.get('growthGoodwill')),
                'intangible_assets': safe_float(growth.get('growthIntangibleAssets')),
                'goodwill_and_intangible_assets': safe_float(growth.get('growthGoodwillAndIntangibleAssets')),
                'long_term_investments': safe_float(growth.get('growthLongTermInvestments')),
                'tax_assets': safe_float(growth.get('growthTaxAssets')),
                'other_non_current_assets': safe_float(growth.get('growthOtherNonCurrentAssets')),
                'total_non_current_assets': safe_float(growth.get('growthTotalNonCurrentAssets')),
                'other_assets': safe_float(growth.get('growthOtherAssets')),
                'total_assets': safe_float(growth.get('growthTotalAssets')),
                'account_payables': safe_float(growth.get('growthAccountPayables')),
                'short_term_debt': safe_float(growth.get('growthShortTermDebt')),
                'tax_payables': safe_float(growth.get('growthTaxPayables')),
                'deferred_revenue': safe_float(growth.get('growthDeferredRevenue')),
                'other_current_liabilities': safe_float(growth.get('growthOtherCurrentLiabilities')),
                'total_current_liabilities': safe_float(growth.get('growthTotalCurrentLiabilities')),
                'long_term_debt': safe_float(growth.get('growthLongTermDebt')),
                'deferred_revenue_non_current': safe_float(growth.get('growthDeferredRevenueNonCurrent')),
                'deferred_tax_liabilities_non_current': safe_float(growth.get('growthDeferredTaxLiabilitiesNonCurrent')),
                'other_non_current_liabilities': safe_float(growth.get('growthOtherNonCurrentLiabilities')),
                'total_non_current_liabilities': safe_float(growth.get('growthTotalNonCurrentLiabilities')),
                'other_liabilities': safe_float(growth.get('growthOtherLiabilities')),
                'total_liabilities': safe_float(growth.get('growthTotalLiabilities')),
                'preferred_stock': safe_float(growth.get('growthPreferredStock')),
                'common_stock': safe_float(growth.get('growthCommonStock')),
                'retained_earnings': safe_float(growth.get('growthRetainedEarnings')),
                'accumulated_other_comprehensive_income_loss': safe_float(growth.get('growthAccumulatedOtherComprehensiveIncomeLoss')),
                'other_total_stockholders_equity': safe_float(growth.get('growthOthertotalStockholdersEquity')),
                'total_stockholders_equity': safe_float(growth.get('growthTotalStockholdersEquity')),
                'minority_interest': safe_float(growth.get('growthMinorityInterest')),
                'total_equity': safe_float(growth.get('growthTotalEquity')),
                'total_liabilities_and_stockholders_equity': safe_float(growth.get('growthTotalLiabilitiesAndStockholdersEquity')),
                'total_investments': safe_float(growth.get('growthTotalInvestments')),
                'total_debt': safe_float(growth.get('growthTotalDebt')),
                'net_debt': safe_float(growth.get('growthNetDebt')),
                'accounts_receivables': safe_float(growth.get('growthAccountsReceivables')),
                'other_receivables': safe_float(growth.get('growthOtherReceivables')),
                'prepaids': safe_float(growth.get('growthPrepaids')),
                'total_payables': safe_float(growth.get('growthTotalPayables')),
                'other_payables': safe_float(growth.get('growthOtherPayables')),
                'accrued_expenses': safe_float(growth.get('growthAccruedExpenses')),
                'capital_lease_obligations_current': safe_float(growth.get('growthCapitalLeaseObligationsCurrent')),
                'additional_paid_in_capital': safe_float(growth.get('growthAdditionalPaidInCapital')),
                'treasury_stock': safe_float(growth.get('growthTreasuryStock'))
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
                "revenue": safe_float(growth.get('growthRevenue')),
                "cost_of_revenue": safe_float(growth.get('growthCostOfRevenue')),
                "gross_profit": safe_float(growth.get('growthGrossProfit')),
                "gross_profit_ratio": safe_float(growth.get('growthGrossProfitRatio')),
                "research_and_development_expenses": safe_float(growth.get('growthResearchAndDevelopmentExpenses')),
                "general_and_administrative_expenses": safe_float(growth.get('growthGeneralAndAdministrativeExpenses')),
                "selling_and_marketing_expenses": safe_float(growth.get('growthSellingAndMarketingExpenses')),
                "other_expenses": safe_float(growth.get('growthOtherExpenses')),
                "operating_expenses": safe_float(growth.get('growthOperatingExpenses')),
                "cost_and_expenses": safe_float(growth.get('growthCostAndExpenses')),
                "interest_income": safe_float(growth.get('growthInterestIncome')),
                "interest_expense": safe_float(growth.get('growthInterestExpense')),
                "depreciation_and_amortization": safe_float(growth.get('growthDepreciationAndAmortization')),
                "ebitda": safe_float(growth.get('growthEBITDA')),
                "operating_income": safe_float(growth.get('growthOperatingIncome')),
                "income_before_tax": safe_float(growth.get('growthIncomeBeforeTax')),
                "income_tax_expense": safe_float(growth.get('growthIncomeTaxExpense')),
                "net_income": safe_float(growth.get('growthNetIncome')),
                "eps": safe_float(growth.get('growthEPS')),
                "eps_diluted": safe_float(growth.get('growthEPSDiluted')),
                "weighted_average_shs_out": safe_float(growth.get('growthWeightedAverageShsOut')),
                "weighted_average_shs_out_diluted": safe_float(growth.get('growthWeightedAverageShsOutDil')),
                "ebit": safe_float(growth.get('growthEBIT')),
                "non_operating_income_excluding_interest": safe_float(growth.get('growthNonOperatingIncomeExcludingInterest')),
                "net_interest_income": safe_float(growth.get('growthNetInterestIncome')),
                "total_other_income_expenses_net": safe_float(growth.get('growthTotalOtherIncomeExpensesNet')),
                "net_income_from_continuing_operations": safe_float(growth.get('growthNetIncomeFromContinuingOperations')),
                "other_adjustments_to_net_income": safe_float(growth.get('growthOtherAdjustmentsToNetIncome')),
                "net_income_deductions": safe_float(growth.get('growthNetIncomeDeductions'))
            }
            translated_growth.append(translated)
        
        return translated_growth 