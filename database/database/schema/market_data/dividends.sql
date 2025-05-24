-- Dividends
CREATE TABLE dividends (
    symbol TEXT,
    date TEXT,
    declaration_date TEXT,
    adj_dividend REAL,
    dividend REAL,
    yield REAL,
    frequency TEXT,
    last_updated TEXT,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);