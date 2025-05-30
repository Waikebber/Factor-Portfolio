-- Cashflow statement growth
CREATE TABLE IF NOT EXISTS cashflow_statement_growth (
    symbol TEXT,
    date TEXT,
    fiscal_year TEXT,
    period TEXT,
    reported_currency TEXT,

    net_income REAL,
    depreciation_and_amortization REAL,
    deferred_income_tax REAL,
    stock_based_compensation REAL,
    change_in_working_capital REAL,
    accounts_receivables REAL,
    inventory REAL,
    accounts_payables REAL,
    other_working_capital REAL,
    other_non_cash_items REAL,
    net_cash_provided_by_operating_activites REAL,

    investments_in_property_plant_and_equipment REAL,
    acquisitions_net REAL,
    purchases_of_investments REAL,
    sales_maturities_of_investments REAL,
    other_investing_activites REAL,
    net_cash_used_for_investing_activites REAL,

    debt_repayment REAL,
    common_stock_issued REAL,
    common_stock_repurchased REAL,
    dividends_paid REAL,
    other_financing_activites REAL,
    net_cash_used_provided_by_financing_activities REAL,

    effect_of_forex_changes_on_cash REAL,
    net_change_in_cash REAL,
    cash_at_end_of_period REAL,
    cash_at_beginning_of_period REAL,

    operating_cash_flow REAL,
    capital_expenditure REAL,
    free_cash_flow REAL,

    net_debt_issuance REAL,
    long_term_net_debt_issuance REAL,
    short_term_net_debt_issuance REAL,
    net_stock_issuance REAL,
    preferred_dividends_paid REAL,
    income_taxes_paid REAL,
    interest_paid REAL,

    PRIMARY KEY (symbol, date, reported_currency),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);