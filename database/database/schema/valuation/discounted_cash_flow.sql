-- Discounted cash flow
CREATE TABLE IF NOT EXISTS discounted_cash_flow (
    symbol TEXT,
    date TEXT,
    dcf REAL,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);