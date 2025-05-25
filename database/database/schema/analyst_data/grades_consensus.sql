CREATE TABLE IF NOT EXISTS grades_consensus (
    symbol TEXT,
    strong_buy INTEGER,
    buy INTEGER,
    hold INTEGER,
    sell INTEGER,
    strong_sell INTEGER,
    consensus TEXT,
    last_updated TEXT,
    PRIMARY KEY (symbol, last_updated),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);
