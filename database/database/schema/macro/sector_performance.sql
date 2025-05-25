-- Sector Performance
CREATE TABLE sector_performance (
    date TEXT,
    sector TEXT,
    exchange TEXT,
    average_change REAL,
    PRIMARY KEY (date, sector, exchange)
);