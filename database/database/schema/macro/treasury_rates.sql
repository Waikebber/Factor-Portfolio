-- Treasury rates
CREATE TABLE IF NOT EXISTS treasury_rates (
    date TEXT PRIMARY KEY,
    month_1 REAL,
    month_2 REAL,
    month_3 REAL,
    month_6 REAL,
    year_1 REAL,
    year_2 REAL,
    year_3 REAL,
    year_5 REAL,
    year_7 REAL,
    year_10 REAL,
    year_20 REAL,
    year_30 REAL
);