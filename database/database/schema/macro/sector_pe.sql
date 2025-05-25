-- Sector PE
CREATE TABLE IF NOT EXISTS sector_pe (
    date TEXT,
    sector TEXT,
    exchange TEXT,
    pe REAL,
    PRIMARY KEY (date, sector, exchange)
);