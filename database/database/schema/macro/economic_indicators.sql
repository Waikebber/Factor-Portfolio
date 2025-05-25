-- Economic indicators
CREATE TABLE IF NOT EXISTS economic_indicators (
    name TEXT,
    date TEXT,
    value REAL,
    PRIMARY KEY (name, date)
);
