-- Tracks update time and system-level metadata
CREATE TABLE IF NOT EXISTS metadata (
    key TEXT PRIMARY KEY,
    value TEXT
);

-- Core stock identity table (1 row per ticker)
CREATE TABLE IF NOT EXISTS stocks (
    ticker TEXT PRIMARY KEY,
    name TEXT,
    sector TEXT,
    industry TEXT,
    exchange TEXT,
    currency TEXT
);

-- Daily adjusted closing prices
CREATE TABLE IF NOT EXISTS price_data (
    date TEXT,
    ticker TEXT,
    adj_close REAL,
    PRIMARY KEY (date, ticker),
    FOREIGN KEY (ticker) REFERENCES stocks(ticker)
);

-- Value factors (e.g., valuation ratios)
CREATE TABLE IF NOT EXISTS value_factors (
    ticker TEXT PRIMARY KEY,
    pe_ratio REAL,
    pb_ratio REAL,
    ev_to_ebitda REAL,
    dividend_yield REAL,
    earnings_yield REAL,
    last_updated TEXT,
    FOREIGN KEY (ticker) REFERENCES stocks(ticker)
);

-- Quality factors
CREATE TABLE IF NOT EXISTS quality_factors (
    ticker TEXT PRIMARY KEY,
    roe REAL,
    roa REAL,
    gross_profitability REAL,
    earnings_stability REAL,
    debt_to_equity REAL,
    last_updated TEXT,
    FOREIGN KEY (ticker) REFERENCES stocks(ticker)
);

-- Growth factors
CREATE TABLE IF NOT EXISTS growth_factors (
    ticker TEXT PRIMARY KEY,
    earnings_growth REAL,
    sales_growth REAL,
    cash_flow_growth REAL,
    last_updated TEXT,
    FOREIGN KEY (ticker) REFERENCES stocks(ticker)
);

-- Profitability factors
CREATE TABLE IF NOT EXISTS profitability_factors (
    ticker TEXT PRIMARY KEY,
    net_margin REAL,
    operating_margin REAL,
    free_cash_flow_yield REAL,
    roic REAL,
    last_updated TEXT,
    FOREIGN KEY (ticker) REFERENCES stocks(ticker)
);

-- Investment/Asset Growth factors
CREATE TABLE IF NOT EXISTS investment_factors (
    ticker TEXT PRIMARY KEY,
    asset_growth_rate REAL,
    capex_to_depreciation REAL,
    rnd_to_sales REAL,
    last_updated TEXT,
    FOREIGN KEY (ticker) REFERENCES stocks(ticker)
);
