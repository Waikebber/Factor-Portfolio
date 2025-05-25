-- Discounted cash flow
CREATE TABLE discounted_cash_flow (
    symbol TEXT,
    date TEXT,
    dcf REAL,
    stock_price REAL,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);