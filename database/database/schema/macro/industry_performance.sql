-- Industry Performance
CREATE TABLE industry_performance (
    date TEXT,
    industry TEXT,
    exchange TEXT,
    average_change REAL,
    last_updated TEXT,
    PRIMARY KEY (date, industry, exchange)
);