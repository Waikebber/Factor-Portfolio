# Stock Database Package

A SQLite-based database package for managing stock market data, including price history and fundamental data for S&P 500 stocks.

## Features

- SQLite database for persistent storage of stock data
- Automatic S&P 500 ticker collection
- Price history storage and retrieval
- Fundamental data storage and retrieval
- Automatic data updates
- Data preparation utilities for factor analysis
- Progress bars for long-running operations

## Installation

The package is part of the factor portfolio project. Make sure you have the required dependencies:

```bash
pip install pandas numpy yfinance tqdm
```

## Usage

### Basic Usage

```python
from database import StockDatabase

# Create database instance
db = StockDatabase()

# Initialize database (creates tables if they don't exist)
db.initialize()

# Get S&P 500 tickers
tickers = db.get_sp500_tickers()

# Update stock data
db.update_stock_data(tickers)

# Get price data
price_data = db.get_price_data(tickers, start_date, end_date)

# Get fundamental data
fundamental_data = db.get_fundamental_data(tickers)
```

### Command Line Interface

The package includes a command-line script for populating and updating the database:

```bash
# Initial population with default settings (3 years of data)
python -m database.populate_database

# Force update all data
python -m database.populate_database --force

# Download 5 years of historical data
python -m database.populate_database --days 1825
```

## Database Structure

The database contains three main tables:

1. `price_data`:
   - `date`: Date of the price
   - `ticker`: Stock symbol
   - `adj_close`: Adjusted closing price

2. `fundamental_data`:
   - `ticker`: Stock symbol (primary key)
   - `market_cap`: Market capitalization
   - `pe_ratio`: Price-to-Earnings ratio
   - `pb_ratio`: Price-to-Book ratio
   - `dividend_yield`: Dividend yield
   - `last_updated`: Timestamp of last update

3. `metadata`:
   - `key`: Metadata key
   - `value`: Metadata value

## API Reference

### StockDatabase Class

Main class for database operations.

#### Methods

- `initialize()`: Initialize database and create tables
- `delete()`: Delete the database file
- `get_last_update()`: Get timestamp of last data update
- `get_sp500_tickers()`: Get list of S&P 500 tickers
- `update_stock_data(tickers, start_date=None, end_date=None)`: Update stock data
- `get_price_data(tickers, start_date=None, end_date=None)`: Get price data
- `get_fundamental_data(tickers)`: Get fundamental data
- `get_available_tickers()`: Get list of available tickers
- `get_data_range()`: Get date range of available data
- `prepare_alpha_data(factor_df, returns, lookback=252)`: Prepare data for alpha modeling

### populate_database Function

High-level function for populating and updating the database.

#### Parameters

- `force_update` (bool): Whether to force update all data
- `days_back` (int): Number of days of historical data to download

## Data Sources

- Price data: Yahoo Finance (yfinance)
- S&P 500 tickers: Wikipedia
- Fundamental data: Yahoo Finance (yfinance)

## Notes

- The database is stored in the package directory as `stock_data.db`
- Data is automatically updated if it's older than 1 day
- Default historical data range is 3 years
- All dates are stored in 'YYYY-MM-DD' format 