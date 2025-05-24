-- Sector PE
CREATE TABLE sector_pe (
    date TEXT,
    sector TEXT,
    exchange TEXT,
    pe REAL,
    last_updated TEXT,
    PRIMARY KEY (date, sector, exchange)
);