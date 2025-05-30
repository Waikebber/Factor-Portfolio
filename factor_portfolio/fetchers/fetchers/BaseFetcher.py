from abc import ABC, abstractmethod
import pandas as pd
from database.database.services import DatabaseGetter

class BaseFetcher(ABC):
    def __init__(self, config: dict = None, getter: DatabaseGetter = None):
        self.config = config or {}
        self.getter = getter if getter else DatabaseGetter()

        # Pre-extract common config values
        self.default_start_date = self.config.get("default_start_date", "2020-01-01")
        self.default_end_date = self.config.get("default_end_date", pd.Timestamp.today().strftime("%Y-%m-%d"))
        self.clean_missing = self.config.get("clean_missing", False)
        self.frequency = self.config.get("frequency", None)

    @abstractmethod
    def fetch(self, symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
        pass

    def fetch_date(self, symbol: str, date: str) -> pd.DataFrame:
        return self.fetch(symbol, date, date)
