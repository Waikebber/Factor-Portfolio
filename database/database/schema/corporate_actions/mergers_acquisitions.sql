-- Mergers and acquisitions
CREATE TABLE mergers_acquisitions (
    symbol TEXT,             -- Acquiring company
    targeted_symbol TEXT,    -- Acquired company
    transaction_date TEXT,
    last_updated TEXT,
    PRIMARY KEY (symbol, targeted_symbol, transaction_date),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);