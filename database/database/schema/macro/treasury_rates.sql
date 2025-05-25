-- Treasury rates
CREATE TABLE treasury_rates (
    date TEXT PRIMARY KEY,
    month1 REAL,
    month2 REAL,
    month3 REAL,
    month6 REAL,
    year1 REAL,
    year2 REAL,
    year3 REAL,
    year5 REAL,
    year7 REAL,
    year10 REAL,
    year20 REAL,
    year30 REAL
);