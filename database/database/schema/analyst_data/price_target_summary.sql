-- Price target summary
CREATE TABLE price_target_summary (
    symbol TEXT PRIMARY KEY,
    last_month_count INTEGER,
    last_month_avg_price_target REAL,
    last_quarter_count INTEGER,
    last_quarter_avg_price_target REAL,
    last_year_count INTEGER,
    last_year_avg_price_target REAL,
    all_time_count INTEGER,
    all_time_avg_price_target REAL,
    last_updated TEXT,
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);