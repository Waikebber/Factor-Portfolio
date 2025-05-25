-- Industry PE
CREATE TABLE IF NOT EXISTS industry_pe (
    date TEXT,
    industry TEXT,
    exchange TEXT,
    pe REAL,
    PRIMARY KEY (date, industry, exchange)
);
