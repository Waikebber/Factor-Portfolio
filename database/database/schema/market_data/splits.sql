-- Splits
CREATE TABLE IF NOT EXISTS splits (
    symbol TEXT,
    date TEXT,
    numerator INTEGER,
    denominator INTEGER,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);
