-- Enterprise values
CREATE TABLE enterprise_values (
    symbol TEXT,
    date TEXT,
    stock_price REAL,
    number_of_shares INTEGER,
    market_capitalization REAL,
    minus_cash_and_cash_equivalents REAL,
    add_total_debt REAL,
    enterprise_value REAL,
    last_updated TEXT,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);