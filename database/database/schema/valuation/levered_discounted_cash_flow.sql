-- Levered discounted cash flow
CREATE TABLE levered_discounted_cash_flow (
    symbol TEXT,
    date TEXT,
    dcf REAL,
    stock_price REAL,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);