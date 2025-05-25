-- Ratings
CREATE TABLE ratings (
    symbol TEXT,
    date TEXT,
    rating TEXT,
    overall_score INTEGER,
    discounted_cash_flow_score INTEGER,
    return_on_equity_score INTEGER,
    return_on_assets_score INTEGER,
    debt_to_equity_score INTEGER,
    price_to_earnings_score INTEGER,
    price_to_book_score INTEGER,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);