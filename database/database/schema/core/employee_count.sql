-- Employee count
CREATE TABLE employee_count (
    symbol TEXT,
    date TEXT,
    employee_count INTEGER,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);