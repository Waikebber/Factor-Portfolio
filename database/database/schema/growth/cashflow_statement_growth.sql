-- Cashflow statement growth
CREATE TABLE cashflow_statement_growth (
    symbol TEXT,
    date TEXT,
    fiscal_year TEXT,
    period TEXT,
    reported_currency TEXT,

    growth_net_income REAL,
    growth_depreciation_and_amortization REAL,
    growth_deferred_income_tax REAL,
    growth_stock_based_compensation REAL,
    growth_change_in_working_capital REAL,
    growth_accounts_receivables REAL,
    growth_inventory REAL,
    growth_accounts_payables REAL,
    growth_other_working_capital REAL,
    growth_other_non_cash_items REAL,
    growth_net_cash_provided_by_operating_activities REAL,

    growth_investments_in_property_plant_and_equipment REAL,
    growth_acquisitions_net REAL,
    growth_purchases_of_investments REAL,
    growth_sales_maturities_of_investments REAL,
    growth_other_investing_activities REAL,
    growth_net_cash_used_for_investing_activities REAL,

    growth_debt_repayment REAL,
    growth_common_stock_issued REAL,
    growth_common_stock_repurchased REAL,
    growth_dividends_paid REAL,
    growth_other_financing_activities REAL,
    growth_net_cash_used_provided_by_financing_activities REAL,

    growth_effect_of_forex_changes_on_cash REAL,
    growth_net_change_in_cash REAL,
    growth_cash_at_end_of_period REAL,
    growth_cash_at_beginning_of_period REAL,

    growth_operating_cash_flow REAL,
    growth_capital_expenditure REAL,
    growth_free_cash_flow REAL,

    growth_net_debt_issuance REAL,
    growth_long_term_net_debt_issuance REAL,
    growth_short_term_net_debt_issuance REAL,
    growth_net_stock_issuance REAL,
    growth_preferred_dividends_paid REAL,
    growth_income_taxes_paid REAL,
    growth_interest_paid REAL,

    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);