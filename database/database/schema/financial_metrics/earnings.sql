-- Earnings
CREATE TABLE IF NOT EXISTS earnings (
    symbol TEXT,
    date TEXT,
    eps_actual REAL,
    eps_estimated REAL,
    revenue_actual REAL,
    revenue_estimated REAL,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);