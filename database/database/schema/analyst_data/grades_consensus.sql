CREATE TABLE grades_consensus (
    symbol TEXT PRIMARY KEY,
    strong_buy INTEGER,
    buy INTEGER,
    hold INTEGER,
    sell INTEGER,
    strong_sell INTEGER,
    consensus TEXT,
    last_updated TEXT,
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);
