import sqlite3
import os
import time
from datetime import datetime, timedelta
from typing import List, Optional
from tqdm import tqdm
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from FinancialCalculations import FinancialCalculations
from .db_writers import *
from .db_getters.StockDataGetter import StockDataGetter
from .db_writers.DataFetcher import DataFetcher

class StockDatabase:
    def __init__(self, db_name='stock_data.db'):
        self.db_name = db_name
        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), db_name)
        self.data_fetcher = DataFetcher()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def initialize(self):
        try:
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            conn = self._get_connection()
            cursor = conn.cursor()
            
            # Get the schema directory path
            schema_dir = os.path.join(os.path.dirname(__file__), "schema")
            
            # Define the order of schema directories to ensure proper table creation
            schema_dirs = [
                'core',           # Core tables first
                'market_data',    # Market data tables
                'financial_metrics', # Financial metrics
                'valuation',      # Valuation tables
                'analyst_data',   # Analyst data
                'corporate_actions', # Corporate actions
                'macro',          # Macro data
                'analysis',       # Analysis tables
                'growth'          # Growth tables
            ]
            
            # Process each directory in order
            for dir_name in schema_dirs:
                dir_path = os.path.join(schema_dir, dir_name)
                if os.path.exists(dir_path):
                    print(f"Processing schema directory: {dir_name}")
                    # Get all SQL files in the directory
                    sql_files = [f for f in os.listdir(dir_path) if f.endswith('.sql')]
                    # Sort files to ensure consistent order
                    sql_files.sort()
                    
                    # Execute each SQL file
                    for sql_file in sql_files:
                        file_path = os.path.join(dir_path, sql_file)
                        print(f"  Executing: {sql_file}")
                        with open(file_path, 'r') as f:
                            cursor.executescript(f.read())
            
            conn.commit()
            conn.close()
            print("Database initialization complete.")
            return True
        except Exception as e:
            print(f"Failed to initialize database: {str(e)}")
            return False

    def delete(self):
        try:
            if os.path.exists(self.db_path):
                os.remove(self.db_path)
            return True
        except Exception as e:
            print(f"Error deleting database: {e}")
            return False

    def update_stock_data(self, tickers: Optional[List[str]] = None, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> bool:
        try:
            if tickers is None:
                tickers = self.data_fetcher.get_sp500_tickers()
            if end_date is None:
                end_date = datetime.now()
            if start_date is None:
                start_date = end_date - timedelta(days=365 * 3)

            print(f"Starting download for {len(tickers)} tickers")
            num_batches = (len(tickers) + self.data_fetcher.batch_size - 1) // self.data_fetcher.batch_size
            
            conn = self._get_connection()
            store_factors = StoreFactors(conn)
            store_prices = StorePrices(conn)
            store_estimates = StoreEstimates(conn)
            store_macro = StoreMacroData(conn)
            data_getter = StockDataGetter(conn)

            with tqdm(total=len(tickers), desc="Overall Progress") as pbar:
                for i in range(0, len(tickers), self.data_fetcher.batch_size):
                    batch = tickers[i:i + self.data_fetcher.batch_size]
                    print(f"\nBatch {i // self.data_fetcher.batch_size + 1} / {num_batches}: {batch}")
                    self.data_fetcher.process_batch(batch, start_date, end_date, store_factors, store_prices, store_estimates, store_macro)
                    pbar.update(len(batch))
                    if i + self.data_fetcher.batch_size < len(tickers):
                        print(f"Sleeping for {self.data_fetcher.batch_delay} seconds...")
                        time.sleep(self.data_fetcher.batch_delay)

            data_getter.update_last_update(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            conn.close()
            print("Update complete.")
            return True
        except Exception as e:
            print(f"Error updating stock data: {e}")
            return False

    def get_getters(self):
        return StockDataGetter(self._get_connection())

    def prepare_alpha_data(self, factor_df, returns, lookback=252):
        return FinancialCalculations.prepare_alpha_data(factor_df, returns, lookback)

if __name__ == "__main__":
    db = StockDatabase()
    db.initialize()
    db.update_stock_data()
