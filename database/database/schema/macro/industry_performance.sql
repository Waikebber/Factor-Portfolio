-- Industry Performance
CREATE TABLE IF NOT EXISTS industry_performance (
    date TEXT,
    industry TEXT,
    exchange TEXT,
    average_change REAL,
    PRIMARY KEY (date, industry, exchange)
);