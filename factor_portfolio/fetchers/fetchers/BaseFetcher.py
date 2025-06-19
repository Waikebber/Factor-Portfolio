from abc import ABC, abstractmethod
import pandas as pd

import os, sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent.parent))
from database.database.services import DatabaseGetter
from database.database.StockDatabase import StockDatabase

class BaseFetcher(ABC):
    def __init__(self, config: dict = None, getter: DatabaseGetter = None):
        self.config = config or {}
        
        # Initialize database with correct path
        db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'database/stock_data.db')
        db = StockDatabase(db_name=db_path)
        
        # Initialize database if it doesn't exist
        if not os.path.exists(db_path):
            db.initialize()
            
        self.getter = getter if getter else DatabaseGetter(db)

        # Pre-extract common config values
        self.default_start_date = self.config.get("default_start_date", "2020-01-01")
        self.default_end_date = self.config.get("default_end_date", "2026-01-01")
        self.clean_missing = self.config.get("clean_missing", False)
        self.frequency = self.config.get("frequency", None)

    @abstractmethod
    def fetch(self, symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
        pass

    def fetch_date(self, symbol: str, date: str) -> pd.DataFrame:
        return self.fetch(symbol, date, date)
    
    def expand_periodic_data(self, price_df: pd.DataFrame, periodic_df: pd.DataFrame) -> pd.DataFrame:
        """
        Expands periodic (e.g. quarterly) data forward in time until the next update.
        For each symbol, forward-fills each column by date.

        Args:
            price_df: Daily price data. Must contain 'symbol' and 'date'.
            periodic_df: Periodic fundamentals. Must contain 'symbol' and 'date' and the columns to expand.

        Returns:
            DataFrame with all periodic columns forward-filled and aligned to price_df dates.
        """
        if periodic_df.empty:
            return price_df.set_index(["symbol", "date"])

        # Ensure proper types and sort
        price_df = price_df.copy()
        periodic_df = periodic_df.copy()
        price_df["date"] = pd.to_datetime(price_df["date"])
        periodic_df["date"] = pd.to_datetime(periodic_df["date"])
        price_df.sort_values(["symbol", "date"], inplace=True)
        periodic_df.sort_values(["symbol", "date"], inplace=True)

        # Columns to propagate
        value_cols = [col for col in periodic_df.columns if col not in {"symbol", "date"}]

        # Output rows
        expanded = []

        for symbol in price_df["symbol"].unique():
            price_sym = price_df[price_df["symbol"] == symbol].copy()
            periodic_sym = periodic_df[periodic_df["symbol"] == symbol].copy()

            if periodic_sym.empty:
                price_sym.set_index(["symbol", "date"], inplace=True)
                expanded.append(price_sym)
                continue

            # Merge on date, forward-fill values
            merged = pd.merge_asof(
                price_sym.sort_values("date"),
                periodic_sym[["date"] + value_cols].sort_values("date"),
                on="date",
                direction="backward"
            )
            merged["symbol"] = symbol
            merged.set_index(["symbol", "date"], inplace=True)
            expanded.append(merged)

        return pd.concat(expanded).sort_index()
