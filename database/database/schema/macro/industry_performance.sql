-- Industry Performance
CREATE TABLE industry_performance (
    date TEXT,
    industry TEXT,
    exchange TEXT,
    average_change REAL,
    PRIMARY KEY (date, industry, exchange)
);