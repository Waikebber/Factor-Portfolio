-- Economic indicators
CREATE TABLE economic_indicators (
    name TEXT,
    date TEXT,
    value REAL,
    PRIMARY KEY (name, date)
);
