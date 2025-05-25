-- Stock identity and metadata
CREATE TABLE IF NOT EXISTS stocks (
    symbol TEXT PRIMARY KEY,
    company_name TEXT,
    exchange_short_name TEXT,
    industry TEXT,
    sector TEXT,
    country TEXT,
    is_actively_trading BOOLEAN,
    last_updated TEXT
);