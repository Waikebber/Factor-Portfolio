-- Grades
CREATE TABLE IF NOT EXISTS grades (
    symbol TEXT,
    date TEXT,
    buy INTEGER,
    hold INTEGER,
    sell INTEGER,
    strong_sell INTEGER,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);