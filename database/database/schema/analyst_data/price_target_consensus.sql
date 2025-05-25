-- Price target consensus
CREATE TABLE price_target_consensus (
    symbol TEXT,
    target_high REAL,
    target_low REAL,
    target_consensus REAL,
    target_median REAL,
    last_updated TEXT,
    PRIMARY KEY (symbol, last_updated),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);