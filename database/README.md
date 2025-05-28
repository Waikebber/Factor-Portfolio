# Stock Database Package

A SQLite-based database package for managing comprehensive stock market data, including price history, fundamental data, financial metrics, and market indicators for stocks.

The database data is derived from the 

## Features

- SQLite database for persistent storage of stock data
- Comprehensive data storage including:
  - Core stock information
  - Market data (prices, dividends, splits)
  - Financial metrics and ratios
  - Valuation metrics
  - Analyst data and estimates
  - Macroeconomic indicators
  - Growth metrics
- Automatic data updates
- Data preparation utilities for factor analysis
- Progress bars for long-running operations

## Installation

The package is part of the factor portfolio project. Make sure you have the required dependencies:

```bash
pip install pandas numpy yfinance tqdm XlsxWriter
```

## Usage

### Basic Usage

```python
from database.StockDatabase import StockDatabase
from database.services import DatabasePopulator

# Create/initialize database instance
db = StockDatabase()
db.initialize()

# Initial Setup Population
populator = DatabasePopulator(db)
populator.set_up_database()

# Populate the table with data from the S&P500
populator.populate_sp500()
```

## Database Structure

The database is organized into several logical sections:

### Core Tables
- `stocks`: Basic stock information (symbol, company name, industry, sector)
- `employee_count`: Historical employee count data

### Market Data Tables
- `prices`: Historical price data (OHLCV)
- `dividends`: Historical dividend data
- `splits`: Stock split history
- `dividend_adjusted_price_data`: Price data adjusted for corporate actions
- `market_cap`: Market capitalization data
- `share_float`: Information about shares available for trading

### Financial Metrics Tables
- `financial_ratios`: Comprehensive financial ratios and metrics
- `key_metrics`: Important financial metrics (revenue, profit, EPS)
- `earnings`: Earnings data

### Valuation Tables
- `discounted_cash_flow`: DCF valuation data
- `levered_discounted_cash_flow`: Levered DCF valuation data
- `enterprise_values`: Enterprise value calculations
- `owner_earnings`: Owner earnings metrics

### Analyst Data Tables
- `grades`: Analyst grades for stocks
- `grades_consensus`: Consensus analyst grades
- `price_target_summary`: Analyst price targets
- `price_target_consensus`: Consensus price targets

### Macro Tables
- `treasury_rates`: Treasury bond rates across different maturities
- `economic_indicators`: Key economic indicators
- `industry_pe`: Industry-wide P/E ratios
- `sector_pe`: Sector-wide P/E ratios
- `industry_performance`: Industry performance metrics
- `sector_performance`: Sector performance metrics
- `mergers_acquisitions`: M&A activity data

### Analysis Tables
- `analyst_ratings`: Detailed analyst ratings and recommendations
- `analyst_estimates`: Detailed analyst estimates for various financial metrics

### Growth Tables
- `financial_statement_growth`: Comprehensive growth metrics for financial statements
- `cashflow_statement_growth`: Growth metrics for cash flow statement items
- `balance_sheet_growth`: Growth metrics for balance sheet items
- `income_statement_growth`: Growth metrics for income statement items