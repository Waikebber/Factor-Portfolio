-- Dividend adjusted price data
CREATE TABLE dividend_adjusted_price_data (
    symbol TEXT,
    date TEXT,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    adj_open REAL,
    adj_high REAL,
    adj_low REAL,
    adj_close REAL,
    volume INTEGER,
    unadjusted_volume INTEGER,
    change REAL,
    change_percent REAL,
    vwap REAL,
    label TEXT,
    change_over_time REAL,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);