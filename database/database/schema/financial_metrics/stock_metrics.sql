-- Stock metrics that change frequently
CREATE TABLE stock_metrics (
    symbol TEXT PRIMARY KEY,
    beta REAL,
    price_range TEXT,
    changes REAL,
    dcf_diff REAL,
    last_updated TEXT,
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);
