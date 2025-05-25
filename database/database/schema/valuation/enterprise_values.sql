-- Enterprise values
CREATE TABLE IF NOT EXISTS enterprise_values (
    symbol TEXT,
    date TEXT,
    number_of_shares INTEGER,
    add_total_debt REAL,
    minus_cash_and_cash_equivalents REAL,
    enterprise_value REAL,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);