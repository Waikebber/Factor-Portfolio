-- Sector Performance
CREATE TABLE sector_performance (
    date TEXT,
    sector TEXT,
    exchange TEXT,
    average_change REAL,
    last_updated TEXT,
    PRIMARY KEY (date, sector, exchange)
);