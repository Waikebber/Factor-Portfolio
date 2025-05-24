# Database Schema Documentation

This document provides a comprehensive overview of all database tables and their columns.

## Table of Contents
- [Core Tables](#core-tables)
- [Market Data Tables](#market-data-tables)
- [Financial Metrics Tables](#financial-metrics-tables)
- [Valuation Tables](#valuation-tables)
- [Analyst Data Tables](#analyst-data-tables)
- [Corporate Actions Tables](#corporate-actions-tables)
- [Macro Tables](#macro-tables)
- [Analysis Tables](#analysis-tables)
- [Growth Tables](#growth-tables)

## Core Tables

### stocks
Primary table containing basic stock information.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Primary key, stock ticker symbol |
| company_name | TEXT | Full company name |
| exchange_short_name | TEXT | Stock exchange identifier |
| industry | TEXT | Company's industry classification |
| sector | TEXT | Company's sector classification |
| country | TEXT | Country of primary listing |
| full_time_employees | INTEGER | Number of full-time employees |
| is_actively_trading | BOOLEAN | Whether the stock is currently trading |
| is_adr | BOOLEAN | Whether the stock is an American Depositary Receipt |
| last_updated | TEXT | Timestamp of last data update |

### employee_count
Tracks historical employee count data.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Date of the employee count |
| employee_count | INTEGER | Number of employees on that date |
| last_updated | TEXT | Timestamp of last data update |

## Market Data Tables

### prices
Historical price data for stocks.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Trading date |
| open | REAL | Opening price |
| high | REAL | Highest price during the day |
| low | REAL | Lowest price during the day |
| close | REAL | Closing price |
| volume | INTEGER | Trading volume |
| last_updated | TEXT | Timestamp of last data update |

### dividends
Historical dividend data.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Dividend payment date |
| amount | REAL | Dividend amount per share |
| last_updated | TEXT | Timestamp of last data update |

### splits
Stock split history.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Split date |
| ratio | TEXT | Split ratio (e.g., "2:1") |
| last_updated | TEXT | Timestamp of last data update |

### dividend_adjusted_price_data
Price data adjusted for dividends and splits.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Trading date |
| adjusted_close | REAL | Price adjusted for dividends and splits |
| last_updated | TEXT | Timestamp of last data update |

### market_cap
Market capitalization data.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Date of market cap |
| market_cap | REAL | Market capitalization value |
| last_updated | TEXT | Timestamp of last data update |

### share_float
Information about shares available for trading.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Date of float data |
| float_shares | INTEGER | Number of shares available for trading |
| last_updated | TEXT | Timestamp of last data update |

## Financial Metrics Tables

### financial_ratios
Key financial ratios.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Date of ratios |
| current_ratio | REAL | Current assets / current liabilities |
| quick_ratio | REAL | (Current assets - inventory) / current liabilities |
| debt_to_equity | REAL | Total debt / total equity |
| return_on_equity | REAL | Net income / total equity |
| return_on_assets | REAL | Net income / total assets |
| last_updated | TEXT | Timestamp of last data update |

### key_metrics
Important financial metrics.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Date of metrics |
| revenue | REAL | Total revenue |
| gross_profit | REAL | Revenue - cost of goods sold |
| operating_income | REAL | Income from operations |
| net_income | REAL | Total net income |
| eps | REAL | Earnings per share |
| last_updated | TEXT | Timestamp of last data update |

### stock_metrics
Stock-specific performance metrics.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Date of metrics |
| beta | REAL | Stock's beta coefficient |
| volatility | REAL | Price volatility measure |
| last_updated | TEXT | Timestamp of last data update |

## Valuation Tables

### discounted_cash_flow
DCF valuation data.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Valuation date |
| dcf_value | REAL | Calculated DCF value |
| last_updated | TEXT | Timestamp of last data update |

### levered_discounted_cash_flow
Levered DCF valuation data.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Valuation date |
| levered_dcf_value | REAL | Calculated levered DCF value |
| last_updated | TEXT | Timestamp of last data update |

### enterprise_values
Enterprise value calculations.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Valuation date |
| enterprise_value | REAL | Total enterprise value |
| last_updated | TEXT | Timestamp of last data update |

### owner_earnings
Owner earnings metrics.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Date of earnings |
| owner_earnings | REAL | Calculated owner earnings |
| last_updated | TEXT | Timestamp of last data update |

## Analyst Data Tables

### grades
Analyst grades for stocks.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Grade date |
| grade | TEXT | Analyst grade |
| last_updated | TEXT | Timestamp of last data update |

### grades_consensus
Consensus analyst grades.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Consensus date |
| consensus_grade | TEXT | Consensus grade |
| last_updated | TEXT | Timestamp of last data update |

### price_target_summary
Analyst price targets.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Target date |
| target_price | REAL | Price target |
| last_updated | TEXT | Timestamp of last data update |

### price_target_consensus
Consensus price targets.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Consensus date |
| consensus_price | REAL | Consensus price target |
| last_updated | TEXT | Timestamp of last data update |

## Corporate Actions Tables

### mergers_acquisitions
M&A activity data.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Announcement date |
| deal_type | TEXT | Type of deal |
| last_updated | TEXT | Timestamp of last data update |

### earnings
Earnings data.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Earnings date |
| eps | REAL | Earnings per share |
| last_updated | TEXT | Timestamp of last data update |

## Macro Tables

### treasury_rates
Treasury bond rates across different maturities.

| Column | Type | Description |
|--------|------|-------------|
| date | TEXT | Primary key, date of rates |
| month1 | REAL | 1-month treasury rate |
| month2 | REAL | 2-month treasury rate |
| month3 | REAL | 3-month treasury rate |
| month6 | REAL | 6-month treasury rate |
| year1 | REAL | 1-year treasury rate |
| year2 | REAL | 2-year treasury rate |
| year3 | REAL | 3-year treasury rate |
| year5 | REAL | 5-year treasury rate |
| year7 | REAL | 7-year treasury rate |
| year10 | REAL | 10-year treasury rate |
| year20 | REAL | 20-year treasury rate |
| year30 | REAL | 30-year treasury rate |
| last_updated | TEXT | Timestamp of last data update |

### economic_indicators
Key economic indicators.

| Column | Type | Description |
|--------|------|-------------|
| date | TEXT | Primary key, date of indicators |
| gdp_growth | REAL | GDP growth rate |
| inflation_rate | REAL | Inflation rate |
| unemployment_rate | REAL | Unemployment rate |
| last_updated | TEXT | Timestamp of last data update |

### industry_pe
Industry-wide P/E ratios.

| Column | Type | Description |
|--------|------|-------------|
| industry | TEXT | Industry name |
| date | TEXT | Date of P/E ratio |
| pe_ratio | REAL | Industry average P/E ratio |
| last_updated | TEXT | Timestamp of last data update |

### sector_pe
Sector-wide P/E ratios.

| Column | Type | Description |
|--------|------|-------------|
| sector | TEXT | Sector name |
| date | TEXT | Date of P/E ratio |
| pe_ratio | REAL | Sector average P/E ratio |
| last_updated | TEXT | Timestamp of last data update |

### industry_performance
Industry performance metrics.

| Column | Type | Description |
|--------|------|-------------|
| industry | TEXT | Industry name |
| date | TEXT | Date of performance data |
| performance | REAL | Industry performance metric |
| last_updated | TEXT | Timestamp of last data update |

### sector_performance
Sector performance metrics.

| Column | Type | Description |
|--------|------|-------------|
| sector | TEXT | Sector name |
| date | TEXT | Date of performance data |
| performance | REAL | Sector performance metric |
| last_updated | TEXT | Timestamp of last data update |

## Analysis Tables

### analyst_ratings
Detailed analyst ratings and recommendations.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Rating date |
| rating | TEXT | Analyst rating |
| target_price | REAL | Price target |
| analyst_name | TEXT | Name of the analyst |
| firm_name | TEXT | Name of the analyst's firm |
| last_updated | TEXT | Timestamp of last data update |

### analyst_estimates
Detailed analyst estimates for various financial metrics.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Estimate date |
| revenue_low | REAL | Low estimate for revenue |
| revenue_high | REAL | High estimate for revenue |
| revenue_avg | REAL | Average estimate for revenue |
| ebitda_low | REAL | Low estimate for EBITDA |
| ebitda_high | REAL | High estimate for EBITDA |
| ebitda_avg | REAL | Average estimate for EBITDA |
| ebit_low | REAL | Low estimate for EBIT |
| ebit_high | REAL | High estimate for EBIT |
| ebit_avg | REAL | Average estimate for EBIT |
| net_income_low | REAL | Low estimate for net income |
| net_income_high | REAL | High estimate for net income |
| net_income_avg | REAL | Average estimate for net income |
| sga_expense_low | REAL | Low estimate for SGA expenses |
| sga_expense_high | REAL | High estimate for SGA expenses |
| sga_expense_avg | REAL | Average estimate for SGA expenses |
| eps_low | REAL | Low estimate for EPS |
| eps_high | REAL | High estimate for EPS |
| eps_avg | REAL | Average estimate for EPS |
| num_analysts_revenue | INTEGER | Number of analysts for revenue |
| num_analysts_eps | INTEGER | Number of analysts for EPS |
| last_updated | TEXT | Timestamp of last data update |

## Growth Tables

### financial_statement_growth
Comprehensive growth metrics for financial statements.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Date of growth data |
| fiscal_year | TEXT | Fiscal year |
| period | TEXT | Financial period |
| reported_currency | TEXT | Currency of reported values |
| revenue_growth | REAL | Revenue growth rate |
| gross_profit_growth | REAL | Gross profit growth rate |
| ebit_growth | REAL | EBIT growth rate |
| operating_income_growth | REAL | Operating income growth rate |
| net_income_growth | REAL | Net income growth rate |
| eps_growth | REAL | EPS growth rate |
| eps_diluted_growth | REAL | Diluted EPS growth rate |
| weighted_average_shares_growth | REAL | Growth in weighted average shares |
| weighted_average_shares_diluted_growth | REAL | Growth in diluted weighted average shares |
| dividends_per_share_growth | REAL | Dividend per share growth rate |
| operating_cash_flow_growth | REAL | Operating cash flow growth rate |
| receivables_growth | REAL | Receivables growth rate |
| inventory_growth | REAL | Inventory growth rate |
| asset_growth | REAL | Total assets growth rate |
| book_value_per_share_growth | REAL | Book value per share growth rate |
| debt_growth | REAL | Debt growth rate |
| rd_expense_growth | REAL | R&D expense growth rate |
| sga_expenses_growth | REAL | SGA expenses growth rate |
| free_cash_flow_growth | REAL | Free cash flow growth rate |
| ten_y_revenue_growth_per_share | REAL | 10-year revenue growth per share |
| five_y_revenue_growth_per_share | REAL | 5-year revenue growth per share |
| three_y_revenue_growth_per_share | REAL | 3-year revenue growth per share |
| ten_y_operating_cf_growth_per_share | REAL | 10-year operating cash flow growth per share |
| five_y_operating_cf_growth_per_share | REAL | 5-year operating cash flow growth per share |
| three_y_operating_cf_growth_per_share | REAL | 3-year operating cash flow growth per share |
| ten_y_net_income_growth_per_share | REAL | 10-year net income growth per share |
| five_y_net_income_growth_per_share | REAL | 5-year net income growth per share |
| three_y_net_income_growth_per_share | REAL | 3-year net income growth per share |
| ten_y_shareholders_equity_growth_per_share | REAL | 10-year shareholders equity growth per share |
| five_y_shareholders_equity_growth_per_share | REAL | 5-year shareholders equity growth per share |
| three_y_shareholders_equity_growth_per_share | REAL | 3-year shareholders equity growth per share |
| ten_y_dividend_per_share_growth_per_share | REAL | 10-year dividend per share growth |
| five_y_dividend_per_share_growth_per_share | REAL | 5-year dividend per share growth |
| three_y_dividend_per_share_growth_per_share | REAL | 3-year dividend per share growth |
| ebitda_growth | REAL | EBITDA growth rate |
| growth_capital_expenditure | REAL | Growth capital expenditure |
| ten_y_bottom_line_net_income_growth_per_share | REAL | 10-year bottom line net income growth per share |
| five_y_bottom_line_net_income_growth_per_share | REAL | 5-year bottom line net income growth per share |
| three_y_bottom_line_net_income_growth_per_share | REAL | 3-year bottom line net income growth per share |
| last_updated | TEXT | Timestamp of last data update |

### cashflow_statement_growth
Growth metrics for cash flow statement items.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Date of growth data |
| fiscal_year | TEXT | Fiscal year |
| period | TEXT | Financial period |
| reported_currency | TEXT | Currency of reported values |
| growth_net_income | REAL | Growth in net income |
| growth_depreciation_and_amortization | REAL | Growth in depreciation and amortization |
| growth_deferred_income_tax | REAL | Growth in deferred income tax |
| growth_stock_based_compensation | REAL | Growth in stock-based compensation |
| growth_change_in_working_capital | REAL | Growth in working capital changes |
| growth_accounts_receivables | REAL | Growth in accounts receivables |
| growth_inventory | REAL | Growth in inventory |
| growth_accounts_payables | REAL | Growth in accounts payables |
| growth_other_working_capital | REAL | Growth in other working capital items |
| growth_other_non_cash_items | REAL | Growth in other non-cash items |
| growth_net_cash_provided_by_operating_activities | REAL | Growth in net cash from operations |
| growth_investments_in_property_plant_and_equipment | REAL | Growth in PP&E investments |
| growth_acquisitions_net | REAL | Growth in net acquisitions |
| growth_purchases_of_investments | REAL | Growth in investment purchases |
| growth_sales_maturities_of_investments | REAL | Growth in investment sales/maturities |
| growth_other_investing_activities | REAL | Growth in other investing activities |
| growth_net_cash_used_for_investing_activities | REAL | Growth in net cash used for investing |
| growth_debt_repayment | REAL | Growth in debt repayment |
| growth_common_stock_issued | REAL | Growth in common stock issuance |
| growth_common_stock_repurchased | REAL | Growth in stock repurchases |
| growth_dividends_paid | REAL | Growth in dividends paid |
| growth_other_financing_activities | REAL | Growth in other financing activities |
| growth_net_cash_used_provided_by_financing_activities | REAL | Growth in net cash from financing |
| growth_effect_of_forex_changes_on_cash | REAL | Growth in forex impact on cash |
| growth_net_change_in_cash | REAL | Growth in net cash change |
| growth_cash_at_end_of_period | REAL | Growth in ending cash balance |
| growth_cash_at_beginning_of_period | REAL | Growth in beginning cash balance |
| growth_operating_cash_flow | REAL | Growth in operating cash flow |
| growth_capital_expenditure | REAL | Growth in capital expenditure |
| growth_free_cash_flow | REAL | Growth in free cash flow |
| growth_net_debt_issuance | REAL | Growth in net debt issuance |
| growth_long_term_net_debt_issuance | REAL | Growth in long-term debt issuance |
| growth_short_term_net_debt_issuance | REAL | Growth in short-term debt issuance |
| growth_net_stock_issuance | REAL | Growth in net stock issuance |
| growth_preferred_dividends_paid | REAL | Growth in preferred dividends paid |
| growth_income_taxes_paid | REAL | Growth in income taxes paid |
| growth_interest_paid | REAL | Growth in interest paid |
| last_updated | TEXT | Timestamp of last data update |

### balance_sheet_growth
Growth metrics for balance sheet items.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Date of growth data |
| fiscal_year | TEXT | Fiscal year |
| period | TEXT | Financial period |
| reported_currency | TEXT | Currency of reported values |
| growth_cash_and_cash_equivalents | REAL | Growth in cash and equivalents |
| growth_short_term_investments | REAL | Growth in short-term investments |
| growth_cash_and_short_term_investments | REAL | Growth in total cash and investments |
| growth_net_receivables | REAL | Growth in net receivables |
| growth_inventory | REAL | Growth in inventory |
| growth_other_current_assets | REAL | Growth in other current assets |
| growth_total_current_assets | REAL | Growth in total current assets |
| growth_property_plant_equipment_net | REAL | Growth in net PP&E |
| growth_goodwill | REAL | Growth in goodwill |
| growth_intangible_assets | REAL | Growth in intangible assets |
| growth_goodwill_and_intangible_assets | REAL | Growth in total goodwill and intangibles |
| growth_long_term_investments | REAL | Growth in long-term investments |
| growth_tax_assets | REAL | Growth in tax assets |
| growth_other_non_current_assets | REAL | Growth in other non-current assets |
| growth_total_non_current_assets | REAL | Growth in total non-current assets |
| growth_other_assets | REAL | Growth in other assets |
| growth_total_assets | REAL | Growth in total assets |
| growth_account_payables | REAL | Growth in accounts payable |
| growth_short_term_debt | REAL | Growth in short-term debt |
| growth_tax_payables | REAL | Growth in tax payables |
| growth_deferred_revenue | REAL | Growth in deferred revenue |
| growth_other_current_liabilities | REAL | Growth in other current liabilities |
| growth_total_current_liabilities | REAL | Growth in total current liabilities |
| growth_long_term_debt | REAL | Growth in long-term debt |
| growth_deferred_revenue_non_current | REAL | Growth in non-current deferred revenue |
| growth_deferred_tax_liabilities_non_current | REAL | Growth in non-current deferred tax liabilities |
| growth_other_non_current_liabilities | REAL | Growth in other non-current liabilities |
| growth_total_non_current_liabilities | REAL | Growth in total non-current liabilities |
| growth_other_liabilities | REAL | Growth in other liabilities |
| growth_total_liabilities | REAL | Growth in total liabilities |
| growth_preferred_stock | REAL | Growth in preferred stock |
| growth_common_stock | REAL | Growth in common stock |
| growth_retained_earnings | REAL | Growth in retained earnings |
| growth_accumulated_other_comprehensive_income_loss | REAL | Growth in accumulated OCI |
| growth_othertotal_stockholders_equity | REAL | Growth in other stockholders' equity |
| growth_total_stockholders_equity | REAL | Growth in total stockholders' equity |
| growth_minority_interest | REAL | Growth in minority interest |
| growth_total_equity | REAL | Growth in total equity |
| growth_total_liabilities_and_stockholders_equity | REAL | Growth in total liabilities and equity |
| growth_total_investments | REAL | Growth in total investments |
| growth_total_debt | REAL | Growth in total debt |
| growth_net_debt | REAL | Growth in net debt |
| growth_accounts_receivables | REAL | Growth in accounts receivable |
| growth_other_receivables | REAL | Growth in other receivables |
| growth_prepaids | REAL | Growth in prepaid expenses |
| growth_total_payables | REAL | Growth in total payables |
| growth_other_payables | REAL | Growth in other payables |
| growth_accrued_expenses | REAL | Growth in accrued expenses |
| growth_capital_lease_obligations_current | REAL | Growth in current capital lease obligations |
| growth_additional_paid_in_capital | REAL | Growth in additional paid-in capital |
| growth_treasury_stock | REAL | Growth in treasury stock |
| last_updated | TEXT | Timestamp of last data update |

### income_statement_growth
Growth metrics for income statement items.

| Column | Type | Description |
|--------|------|-------------|
| symbol | TEXT | Foreign key to stocks table |
| date | TEXT | Date of growth data |
| fiscal_year | TEXT | Fiscal year |
| period | TEXT | Financial period |
| reported_currency | TEXT | Currency of reported values |
| growth_revenue | REAL | Growth in revenue |
| growth_cost_of_revenue | REAL | Growth in cost of revenue |
| growth_gross_profit | REAL | Growth in gross profit |
| growth_gross_profit_ratio | REAL | Growth in gross profit ratio |
| growth_research_and_development_expenses | REAL | Growth in R&D expenses |
| growth_general_and_administrative_expenses | REAL | Growth in G&A expenses |
| growth_selling_and_marketing_expenses | REAL | Growth in S&M expenses |
| growth_other_expenses | REAL | Growth in other expenses |
| growth_operating_expenses | REAL | Growth in operating expenses |
| growth_cost_and_expenses | REAL | Growth in total costs and expenses |
| growth_interest_income | REAL | Growth in interest income |
| growth_interest_expense | REAL | Growth in interest expense |
| growth_depreciation_and_amortization | REAL | Growth in depreciation and amortization |
| growth_ebitda | REAL | Growth in EBITDA |
| growth_operating_income | REAL | Growth in operating income |
| growth_income_before_tax | REAL | Growth in income before tax |
| growth_income_tax_expense | REAL | Growth in income tax expense |
| growth_net_income | REAL | Growth in net income |
| growth_eps | REAL | Growth in EPS |
| growth_eps_diluted | REAL | Growth in diluted EPS |
| growth_weighted_average_shs_out | REAL | Growth in weighted average shares outstanding |
| growth_weighted_average_shs_out_dil | REAL | Growth in diluted weighted average shares |
| growth_ebit | REAL | Growth in EBIT |
| growth_non_operating_income_excluding_interest | REAL | Growth in non-operating income |
| growth_net_interest_income | REAL | Growth in net interest income |
| growth_total_other_income_expenses_net | REAL | Growth in net other income/expenses |
| growth_net_income_from_continuing_operations | REAL | Growth in net income from continuing operations |
| growth_other_adjustments_to_net_income | REAL | Growth in other net income adjustments |
| growth_net_income_deductions | REAL | Growth in net income deductions |
| last_updated | TEXT | Timestamp of last data update |

## Notes
- All tables include a `last_updated`