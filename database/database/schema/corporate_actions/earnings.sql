-- Earnings
CREATE TABLE earnings (
    symbol TEXT,
    date TEXT,
    eps_actual REAL,
    eps_estimated REAL,
    revenue_actual REAL,
    revenue_estimated REAL,
    last_updated TEXT,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);