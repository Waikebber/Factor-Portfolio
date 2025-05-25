-- Sector Performance
CREATE TABLE IF NOT EXISTS sector_performance (
    date TEXT,
    sector TEXT,
    exchange TEXT,
    average_change REAL,
    PRIMARY KEY (date, sector, exchange)
);