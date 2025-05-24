-- Stock identity and metadata
CREATE TABLE stocks (
    symbol TEXT PRIMARY KEY,
    company_name TEXT,
    exchange_short_name TEXT,
    industry TEXT,
    sector TEXT,
    country TEXT,
    full_time_employees INTEGER,
    is_actively_trading BOOLEAN,
    is_adr BOOLEAN,
    last_updated TEXT
);