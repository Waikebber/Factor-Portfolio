-- Financial ratios
CREATE TABLE financial_ratios (
    symbol TEXT,
    date TEXT,
    fiscal_year TEXT,
    period TEXT,
    reported_currency TEXT,

    -- Profitability & Margins
    gross_profit_margin REAL,
    ebit_margin REAL,
    ebitda_margin REAL,
    operating_profit_margin REAL,
    pretax_profit_margin REAL,
    continuous_operations_profit_margin REAL,
    net_profit_margin REAL,
    bottom_line_profit_margin REAL,

    -- Turnover Ratios
    receivables_turnover REAL,
    payables_turnover REAL,
    inventory_turnover REAL,
    fixed_asset_turnover REAL,
    asset_turnover REAL,

    -- Liquidity Ratios
    current_ratio REAL,
    quick_ratio REAL,
    solvency_ratio REAL,
    cash_ratio REAL,

    -- Valuation Ratios
    price_to_earnings_ratio REAL,
    price_to_earnings_growth_ratio REAL,
    forward_price_to_earnings_growth_ratio REAL,
    price_to_book_ratio REAL,
    price_to_sales_ratio REAL,
    price_to_free_cash_flow_ratio REAL,
    price_to_operating_cash_flow_ratio REAL,

    -- Leverage Ratios
    debt_to_assets_ratio REAL,
    debt_to_equity_ratio REAL,
    debt_to_capital_ratio REAL,
    long_term_debt_to_capital_ratio REAL,
    financial_leverage_ratio REAL,
    debt_to_market_cap REAL,

    -- Cash Flow Ratios
    working_capital_turnover_ratio REAL,
    operating_cash_flow_ratio REAL,
    operating_cash_flow_sales_ratio REAL,
    free_cash_flow_operating_cash_flow_ratio REAL,
    debt_service_coverage_ratio REAL,
    interest_coverage_ratio REAL,
    short_term_operating_cash_flow_coverage_ratio REAL,
    operating_cash_flow_coverage_ratio REAL,
    capital_expenditure_coverage_ratio REAL,
    dividend_paid_and_capex_coverage_ratio REAL,

    -- Dividend Ratios
    dividend_payout_ratio REAL,
    dividend_yield REAL,
    dividend_yield_percentage REAL,

    -- Per Share Metrics
    revenue_per_share REAL,
    net_income_per_share REAL,
    interest_debt_per_share REAL,
    cash_per_share REAL,
    book_value_per_share REAL,
    tangible_book_value_per_share REAL,
    shareholders_equity_per_share REAL,
    operating_cash_flow_per_share REAL,
    capex_per_share REAL,
    free_cash_flow_per_share REAL,

    -- Tax & Adjustment Metrics
    net_income_per_ebt REAL,
    ebt_per_ebit REAL,
    price_to_fair_value REAL,
    effective_tax_rate REAL,
    enterprise_value_multiple REAL,

    last_updated TEXT,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);