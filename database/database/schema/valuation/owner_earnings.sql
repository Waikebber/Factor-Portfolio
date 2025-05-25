-- Owner earnings
CREATE TABLE IF NOT EXISTS owner_earnings (
    symbol TEXT,
    date TEXT,
    period TEXT,
    fiscal_year TEXT,
    avg_ppe REAL,
    growth_capex REAL,
    maintenance_capex REAL,
    owners_earnings REAL,
    owners_earnings_per_share REAL,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);