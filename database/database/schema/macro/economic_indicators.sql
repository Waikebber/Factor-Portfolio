-- Economic indicators
CREATE TABLE economic_indicators (
    name TEXT,
    date TEXT,
    value REAL,
    last_updated TEXT,
    PRIMARY KEY (name, date)
);
