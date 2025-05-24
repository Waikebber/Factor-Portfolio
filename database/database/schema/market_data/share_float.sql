-- Shares float
CREATE TABLE share_float (
    symbol TEXT,
    date TEXT,
    free_float REAL,
    float_shares INTEGER,
    outstanding_shares INTEGER,
    last_updated TEXT,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);