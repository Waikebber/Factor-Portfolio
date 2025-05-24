-- Industry PE
CREATE TABLE industry_pe (
    date TEXT,
    industry TEXT,
    exchange TEXT,
    pe REAL,
    last_updated TEXT,
    PRIMARY KEY (date, industry, exchange)
);
