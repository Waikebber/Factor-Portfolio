-- Shares float
CREATE TABLE IF NOT EXISTS share_float (
    symbol TEXT,
    date TEXT,
    free_float REAL,
    float_shares INTEGER,
    outstanding_shares INTEGER,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);