from typing import Dict, Any, List
from .utils import safe_float, safe_int

class FinancialMetricsTranslator:
    @staticmethod
    def translate_stock_metrics(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates stock metrics data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw stock metrics data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated stock metrics data in the database schema format
        """
        if not data:
            return []
        
        translated_metrics = []
        for metric in data:
            translated = {
                'symbol': metric.get('symbol'),
                'date': metric.get('date'),
                'beta': safe_float(metric.get('beta')),
                'volatility': safe_float(metric.get('volatility')),
                'shares_outstanding': safe_int(metric.get('sharesOutstanding')),
                'shares_float': safe_int(metric.get('sharesFloat')),
                'shares_short': safe_int(metric.get('sharesShort')),
                'shares_short_prior_month': safe_int(metric.get('sharesShortPriorMonth')),
                'short_ratio': safe_float(metric.get('shortRatio')),
                'short_percent_outstanding': safe_float(metric.get('shortPercentOutstanding')),
                'short_percent_float': safe_float(metric.get('shortPercentFloat')),
                'percent_insiders': safe_float(metric.get('percentInsiders')),
                'percent_institutions': safe_float(metric.get('percentInstitutions')),
                'forward_annual_dividend_rate': safe_float(metric.get('forwardAnnualDividendRate')),
                'forward_annual_dividend_yield': safe_float(metric.get('forwardAnnualDividendYield')),
                'payout_ratio': safe_float(metric.get('payoutRatio')),
                'dividend_date': metric.get('dividendDate'),
                'ex_dividend_date': metric.get('exDividendDate'),
                'last_split_factor': metric.get('lastSplitFactor'),
                'last_split_date': metric.get('lastSplitDate'),
            }
            translated_metrics.append(translated)
        
        return translated_metrics

    @staticmethod
    def translate_financial_ratios(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates financial ratios data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw financial ratios data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated financial ratios data in the database schema format
        """
        if not data:
            return []
        
        translated_ratios = []
        for ratio in data:
            translated = {
                'symbol': ratio.get('symbol'),
                'date': ratio.get('date'),
                'fiscal_year': ratio.get('fiscalYear'),
                'period': ratio.get('period'),
                'reported_currency': ratio.get('reportedCurrency'),
                'gross_profit_margin': safe_float(ratio.get('grossProfitMargin')),
                'ebit_margin': safe_float(ratio.get('ebitMargin')),
                'ebitda_margin': safe_float(ratio.get('ebitdaMargin')),
                'operating_profit_margin': safe_float(ratio.get('operatingProfitMargin')),
                'pretax_profit_margin': safe_float(ratio.get('pretaxProfitMargin')),
                'continuous_operations_profit_margin': safe_float(ratio.get('continuousOperationsProfitMargin')),
                'net_profit_margin': safe_float(ratio.get('netProfitMargin')),
                'bottom_line_profit_margin': safe_float(ratio.get('bottomLineProfitMargin')),
                'receivables_turnover': safe_float(ratio.get('receivablesTurnover')),
                'payables_turnover': safe_float(ratio.get('payablesTurnover')),
                'inventory_turnover': safe_float(ratio.get('inventoryTurnover')),
                'fixed_asset_turnover': safe_float(ratio.get('fixedAssetTurnover')),
                'asset_turnover': safe_float(ratio.get('assetTurnover')),
                'current_ratio': safe_float(ratio.get('currentRatio')),
                'quick_ratio': safe_float(ratio.get('quickRatio')),
                'solvency_ratio': safe_float(ratio.get('solvencyRatio')),
                'cash_ratio': safe_float(ratio.get('cashRatio')),
                'price_to_earnings_ratio': safe_float(ratio.get('priceToEarningsRatio')),
                'price_to_earnings_growth_ratio': safe_float(ratio.get('priceToEarningsGrowthRatio')),
                'forward_price_to_earnings_growth_ratio': safe_float(ratio.get('forwardPriceToEarningsGrowthRatio')),
                'price_to_book_ratio': safe_float(ratio.get('priceToBookRatio')),
                'price_to_sales_ratio': safe_float(ratio.get('priceToSalesRatio')),
                'price_to_free_cash_flow_ratio': safe_float(ratio.get('priceToFreeCashFlowRatio')),
                'price_to_operating_cash_flow_ratio': safe_float(ratio.get('priceToOperatingCashFlowRatio')),
                'debt_to_assets_ratio': safe_float(ratio.get('debtToAssetsRatio')),
                'debt_to_equity_ratio': safe_float(ratio.get('debtToEquityRatio')),
                'debt_to_capital_ratio': safe_float(ratio.get('debtToCapitalRatio')),
                'long_term_debt_to_capital_ratio': safe_float(ratio.get('longTermDebtToCapitalRatio')),
                'financial_leverage_ratio': safe_float(ratio.get('financialLeverageRatio')),
                'debt_to_market_cap': safe_float(ratio.get('debtToMarketCap')),
                'working_capital_turnover_ratio': safe_float(ratio.get('workingCapitalTurnoverRatio')),
                'operating_cash_flow_ratio': safe_float(ratio.get('operatingCashFlowRatio')),
                'operating_cash_flow_sales_ratio': safe_float(ratio.get('operatingCashFlowSalesRatio')),
                'free_cash_flow_operating_cash_flow_ratio': safe_float(ratio.get('freeCashFlowOperatingCashFlowRatio')),
                'debt_service_coverage_ratio': safe_float(ratio.get('debtServiceCoverageRatio')),
                'interest_coverage_ratio': safe_float(ratio.get('interestCoverageRatio')),
                'short_term_operating_cash_flow_coverage_ratio': safe_float(ratio.get('shortTermOperatingCashFlowCoverageRatio')),
                'operating_cash_flow_coverage_ratio': safe_float(ratio.get('operatingCashFlowCoverageRatio')),
                'capital_expenditure_coverage_ratio': safe_float(ratio.get('capitalExpenditureCoverageRatio')),
                'dividend_paid_and_capex_coverage_ratio': safe_float(ratio.get('dividendPaidAndCapexCoverageRatio')),
                'dividend_payout_ratio': safe_float(ratio.get('dividendPayoutRatio')),
                'dividend_yield': safe_float(ratio.get('dividendYield')),
                'dividend_yield_percentage': safe_float(ratio.get('dividendYieldPercentage')),
                'revenue_per_share': safe_float(ratio.get('revenuePerShare')),
                'net_income_per_share': safe_float(ratio.get('netIncomePerShare')),
                'interest_debt_per_share': safe_float(ratio.get('interestDebtPerShare')),
                'cash_per_share': safe_float(ratio.get('cashPerShare')),
                'book_value_per_share': safe_float(ratio.get('bookValuePerShare')),
                'tangible_book_value_per_share': safe_float(ratio.get('tangibleBookValuePerShare')),
                'shareholders_equity_per_share': safe_float(ratio.get('shareholdersEquityPerShare')),
                'operating_cash_flow_per_share': safe_float(ratio.get('operatingCashFlowPerShare')),
                'capex_per_share': safe_float(ratio.get('capexPerShare')),
                'free_cash_flow_per_share': safe_float(ratio.get('freeCashFlowPerShare')),
                'net_income_per_ebt': safe_float(ratio.get('netIncomePerEBT')),
                'ebt_per_ebit': safe_float(ratio.get('ebtPerEbit')),
                'price_to_fair_value': safe_float(ratio.get('priceToFairValue')),
                'effective_tax_rate': safe_float(ratio.get('effectiveTaxRate')),
                'enterprise_value_multiple': safe_float(ratio.get('enterpriseValueMultiple')),
            }
            translated_ratios.append(translated)
        
        return translated_ratios

    @staticmethod
    def translate_key_metrics(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates key metrics data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw key metrics data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated key metrics data in the database schema format
        """
        if not data:
            return []
        
        translated_metrics = []
        for metrics in data:
            translated = {
                'symbol': metrics.get('symbol'),
                'date': metrics.get('date'),
                'fiscal_year': metrics.get('fiscalYear'),
                'period': metrics.get('period'),
                'reported_currency': metrics.get('reportedCurrency'),
                'market_cap': safe_float(metrics.get('marketCap')),
                'enterprise_value': safe_float(metrics.get('enterpriseValue')),
                'ev_to_sales': safe_float(metrics.get('evToSales')),
                'ev_to_operating_cash_flow': safe_float(metrics.get('evToOperatingCashFlow')),
                'ev_to_free_cash_flow': safe_float(metrics.get('evToFreeCashFlow')),
                'ev_to_ebitda': safe_float(metrics.get('evToEBITDA')),
                'net_debt_to_ebitda': safe_float(metrics.get('netDebtToEBITDA')),
                'current_ratio': safe_float(metrics.get('currentRatio')),
                'income_quality': safe_float(metrics.get('incomeQuality')),
                'graham_number': safe_float(metrics.get('grahamNumber')),
                'graham_net_net': safe_float(metrics.get('grahamNetNet')),
                'tax_burden': safe_float(metrics.get('taxBurden')),
                'interest_burden': safe_float(metrics.get('interestBurden')),
                'working_capital': safe_float(metrics.get('workingCapital')),
                'invested_capital': safe_float(metrics.get('investedCapital')),
                'return_on_assets': safe_float(metrics.get('returnOnAssets')),
                'operating_return_on_assets': safe_float(metrics.get('operatingReturnOnAssets')),
                'return_on_tangible_assets': safe_float(metrics.get('returnOnTangibleAssets')),
                'return_on_equity': safe_float(metrics.get('returnOnEquity')),
                'return_on_invested_capital': safe_float(metrics.get('returnOnInvestedCapital')),
                'return_on_capital_employed': safe_float(metrics.get('returnOnCapitalEmployed')),
                'earnings_yield': safe_float(metrics.get('earningsYield')),
                'free_cash_flow_yield': safe_float(metrics.get('freeCashFlowYield')),
                'capex_to_operating_cash_flow': safe_float(metrics.get('capexToOperatingCashFlow')),
                'capex_to_depreciation': safe_float(metrics.get('capexToDepreciation')),
                'capex_to_revenue': safe_float(metrics.get('capexToRevenue')),
                'sga_to_revenue': safe_float(metrics.get('salesGeneralAndAdministrativeToRevenue')),
                'rnd_to_revenue': safe_float(metrics.get('researchAndDevelopementToRevenue')),
                'sbc_to_revenue': safe_float(metrics.get('stockBasedCompensationToRevenue')),
                'intangibles_to_total_assets': safe_float(metrics.get('intangiblesToTotalAssets')),
                'average_receivables': safe_float(metrics.get('averageReceivables')),
                'average_payables': safe_float(metrics.get('averagePayables')),
                'average_inventory': safe_float(metrics.get('averageInventory')),
                'dso': safe_float(metrics.get('daysOfSalesOutstanding')),
                'dpo': safe_float(metrics.get('daysOfPayablesOutstanding')),
                'dio': safe_float(metrics.get('daysOfInventoryOutstanding')),
                'operating_cycle': safe_float(metrics.get('operatingCycle')),
                'cash_conversion_cycle': safe_float(metrics.get('cashConversionCycle')),
                'fcf_to_equity': safe_float(metrics.get('freeCashFlowToEquity')),
                'fcf_to_firm': safe_float(metrics.get('freeCashFlowToFirm')),
                'tangible_asset_value': safe_float(metrics.get('tangibleAssetValue')),
                'net_current_asset_value': safe_float(metrics.get('netCurrentAssetValue')),
            }
            translated_metrics.append(translated)
        return translated_metrics

    @staticmethod
    def translate_earnings(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates earnings data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw earnings data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated earnings data in the database schema format
        """
        if not data:
            return []
        
        translated_earnings = []
        for earnings in data:
            translated = {
                'symbol': earnings.get('symbol'),
                'date': earnings.get('date'),
                'eps_actual': safe_float(earnings.get('epsActual')),
                'eps_estimated': safe_float(earnings.get('epsEstimated')),
                'revenue_actual': safe_float(earnings.get('revenueActual')),
                'revenue_estimated': safe_float(earnings.get('revenueEstimated')),
            }
            translated_earnings.append(translated)
        
        return translated_earnings 