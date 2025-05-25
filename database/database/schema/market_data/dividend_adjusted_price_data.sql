-- Dividend adjusted price data
CREATE TABLE IF NOT EXISTS dividend_adjusted_price_data (
    symbol TEXT,
    date TEXT,
    adj_open REAL,
    adj_high REAL,
    adj_low REAL,
    adj_close REAL,
    volume INTEGER,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);