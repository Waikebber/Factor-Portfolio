-- Owner earnings
CREATE TABLE owner_earnings (
    symbol TEXT,
    date TEXT,
    fiscal_year TEXT,
    period TEXT,
    reported_currency TEXT,
    average_ppe REAL,
    maintenance_capex REAL,
    owners_earnings REAL,
    growth_capex REAL,
    owners_earnings_per_share REAL,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);