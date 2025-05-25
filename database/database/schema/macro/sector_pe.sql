-- Sector PE
CREATE TABLE sector_pe (
    date TEXT,
    sector TEXT,
    exchange TEXT,
    pe REAL,
    PRIMARY KEY (date, sector, exchange)
);