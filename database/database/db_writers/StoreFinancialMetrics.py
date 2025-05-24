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
                    enterprise_value_multiple, last_updated
                ) VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now')
                )
            """, (
                data.get("symbol"), data.get("date"), data.get("fiscalYear"), data.get("period"), data.get("reportedCurrency"),
                data.get("grossProfitMargin"), data.get("ebitMargin"), data.get("ebitdaMargin"), data.get("operatingProfitMargin"),
                data.get("pretaxProfitMargin"), data.get("continuousOperationsProfitMargin"), data.get("netProfitMargin"),
                data.get("bottomLineProfitMargin"), data.get("receivablesTurnover"), data.get("payablesTurnover"),
                data.get("inventoryTurnover"), data.get("fixedAssetTurnover"), data.get("assetTurnover"), data.get("currentRatio"),
                data.get("quickRatio"), data.get("solvencyRatio"), data.get("cashRatio"), data.get("priceToEarningsRatio"),
                data.get("priceToEarningsGrowthRatio"), data.get("forwardPriceToEarningsGrowthRatio"),
                data.get("priceToBookRatio"), data.get("priceToSalesRatio"), data.get("priceToFreeCashFlowRatio"),
                data.get("priceToOperatingCashFlowRatio"), data.get("debtToAssetsRatio"), data.get("debtToEquityRatio"),
                data.get("debtToCapitalRatio"), data.get("longTermDebtToCapitalRatio"), data.get("financialLeverageRatio"),
                data.get("debtToMarketCap"), data.get("workingCapitalTurnoverRatio"), data.get("operatingCashFlowRatio"),
                data.get("operatingCashFlowSalesRatio"), data.get("freeCashFlowOperatingCashFlowRatio"),
                data.get("debtServiceCoverageRatio"), data.get("interestCoverageRatio"),
                data.get("shortTermOperatingCashFlowCoverageRatio"), data.get("operatingCashFlowCoverageRatio"),
                data.get("capitalExpenditureCoverageRatio"), data.get("dividendPaidAndCapexCoverageRatio"),
                data.get("dividendPayoutRatio"), data.get("dividendYield"), data.get("dividendYieldPercentage"),
                data.get("revenuePerShare"), data.get("netIncomePerShare"), data.get("interestDebtPerShare"),
                data.get("cashPerShare"), data.get("bookValuePerShare"), data.get("tangibleBookValuePerShare"),
                data.get("shareholdersEquityPerShare"), data.get("operatingCashFlowPerShare"),
                data.get("capexPerShare"), data.get("freeCashFlowPerShare"), data.get("netIncomePerEBT"),
                data.get("ebtPerEbit"), data.get("priceToFairValue"), data.get("effectiveTaxRate"),
                data.get("enterpriseValueMultiple")
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
                    fcf_to_equity, fcf_to_firm, tangible_asset_value, net_current_asset_value,
                    last_updated
                ) VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now')
                )
            """, (
                data.get("symbol"), data.get("date"), data.get("fiscalYear"), data.get("period"), data.get("reportedCurrency"),
                data.get("marketCap"), data.get("enterpriseValue"), data.get("evToSales"), data.get("evToOperatingCashFlow"),
                data.get("evToFreeCashFlow"), data.get("evToEBITDA"), data.get("netDebtToEBITDA"), data.get("currentRatio"),
                data.get("incomeQuality"), data.get("grahamNumber"), data.get("grahamNetNet"), data.get("taxBurden"),
                data.get("interestBurden"), data.get("workingCapital"), data.get("investedCapital"), data.get("returnOnAssets"),
                data.get("operatingReturnOnAssets"), data.get("returnOnTangibleAssets"), data.get("returnOnEquity"),
                data.get("returnOnInvestedCapital"), data.get("returnOnCapitalEmployed"), data.get("earningsYield"),
                data.get("freeCashFlowYield"), data.get("capexToOperatingCashFlow"), data.get("capexToDepreciation"),
                data.get("capexToRevenue"), data.get("salesGeneralAndAdministrativeToRevenue"), data.get("researchAndDevelopementToRevenue"),
                data.get("stockBasedCompensationToRevenue"), data.get("intangiblesToTotalAssets"), data.get("averageReceivables"),
                data.get("averagePayables"), data.get("averageInventory"), data.get("daysOfSalesOutstanding"), data.get("daysOfPayablesOutstanding"),
                data.get("daysOfInventoryOutstanding"), data.get("operatingCycle"), data.get("cashConversionCycle"),
                data.get("freeCashFlowToEquity"), data.get("freeCashFlowToFirm"), data.get("tangibleAssetValue"),
                data.get("netCurrentAssetValue")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing key metrics for {data.get('symbol')} on {data.get('date')}: {e}")

    def store_stock_metrics(self, data: Dict[str, Any]):
        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO stock_metrics (
                    symbol, beta, price_range, changes, dcf_diff, last_updated
                ) VALUES (?, ?, ?, ?, ?, datetime('now'))
            """, (
                data.get("symbol"),
                data.get("beta"),
                data.get("price_range"),
                data.get("changes"),
                data.get("dcf_diff")
            ))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Error storing stock metrics for {data.get('symbol')}: {e}")
