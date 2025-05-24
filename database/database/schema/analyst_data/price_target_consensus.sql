-- Price target consensus
CREATE TABLE price_target_consensus (
    symbol TEXT PRIMARY KEY,
    target_high REAL,
    target_low REAL,
    target_consensus REAL,
    target_median REAL,
    last_updated TEXT,
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);