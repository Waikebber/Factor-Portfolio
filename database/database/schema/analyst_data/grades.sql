-- Grades
CREATE TABLE grades (
    symbol TEXT,
    date TEXT,
    analyst_ratings_buy INTEGER,
    analyst_ratings_hold INTEGER,
    analyst_ratings_sell INTEGER,
    analyst_ratings_strong_sell INTEGER,
    last_updated TEXT,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);