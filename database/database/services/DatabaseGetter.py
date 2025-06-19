from ..StockDatabase import StockDatabase
from ..db_getters import *
from ..data_fetchers.WikiFetcher import WikiFetcher

class DatabaseGetter:
    def __init__(self, db: StockDatabase):
        self.db = db
        conn = self.db._get_connection()

        # All getter categories
        self.analysis = GetAnalysis(conn)
        self.core = GetCore(conn)
        self.analyst_data = GetAnalystData(conn)
        self.financial_metrics = GetFinancialMetrics(conn)
        self.growth = GetGrowth(conn)
        self.macro = GetMacroData(conn)
        self.market_data = GetMarketData(conn)
        self.valuation = GetValuation(conn)

        wiki_fetcher = WikiFetcher()
        self.ticker = wiki_fetcher.get_sp500_tickers()

