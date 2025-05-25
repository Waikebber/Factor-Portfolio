-- Market cap
CREATE TABLE IF NOT EXISTS market_cap (
    symbol TEXT,
    date TEXT,
    market_cap REAL,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);