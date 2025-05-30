-- Financial statement growth
CREATE TABLE IF NOT EXISTS financial_statement_growth (
    symbol TEXT,
    date TEXT,
    fiscal_year TEXT,
    period TEXT,
    reported_currency TEXT,

    revenue_growth REAL,
    gross_profit_growth REAL,
    ebit_growth REAL,
    operating_income_growth REAL,
    net_income_growth REAL,
    eps_growth REAL,
    eps_diluted_growth REAL,
    weighted_average_shares_growth REAL,
    weighted_average_shares_diluted_growth REAL,
    dividends_per_share_growth REAL,
    operating_cash_flow_growth REAL,
    receivables_growth REAL,
    inventory_growth REAL,
    asset_growth REAL,
    book_value_per_share_growth REAL,
    debt_growth REAL,
    rd_expense_growth REAL,
    sga_expenses_growth REAL,
    free_cash_flow_growth REAL,

    ten_y_revenue_growth_per_share REAL,
    five_y_revenue_growth_per_share REAL,
    three_y_revenue_growth_per_share REAL,
    ten_y_operating_cf_growth_per_share REAL,
    five_y_operating_cf_growth_per_share REAL,
    three_y_operating_cf_growth_per_share REAL,
    ten_y_net_income_growth_per_share REAL,
    five_y_net_income_growth_per_share REAL,
    three_y_net_income_growth_per_share REAL,
    ten_y_shareholders_equity_growth_per_share REAL,
    five_y_shareholders_equity_growth_per_share REAL,
    three_y_shareholders_equity_growth_per_share REAL,
    ten_y_dividend_per_share_growth_per_share REAL,
    five_y_dividend_per_share_growth_per_share REAL,
    three_y_dividend_per_share_growth_per_share REAL,

    ebitda_growth REAL,
    growth_capital_expenditure REAL,
    ten_y_bottom_line_net_income_growth_per_share REAL,
    five_y_bottom_line_net_income_growth_per_share REAL,
    three_y_bottom_line_net_income_growth_per_share REAL,

    PRIMARY KEY (symbol, date, reported_currency),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);