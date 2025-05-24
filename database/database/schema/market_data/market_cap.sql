-- Market cap
CREATE TABLE market_cap (
    symbol TEXT,
    date TEXT,
    market_cap REAL,
    last_updated TEXT,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);