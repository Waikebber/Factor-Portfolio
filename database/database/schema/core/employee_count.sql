-- Employee count
CREATE TABLE IF NOT EXISTS employee_count (
    symbol TEXT,
    period_of_report TEXT,
    employee_count INTEGER,
    PRIMARY KEY (symbol, period_of_report),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);