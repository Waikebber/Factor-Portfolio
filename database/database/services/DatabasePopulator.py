from datetime import datetime, timedelta
import logging
import pandas as pd
from typing import Dict, Any, Optional, List, Callable
from ..StockDatabase import StockDatabase
from ..db_writers import *
from ..data_fetchers.FMPFetcher import FMPFetcher
from ..processing.AnalysisProcessor import AnalysisProcessor

class DatabasePopulator:
    """
    Service class responsible for orchestrating the database population process.
    Coordinates data fetching, transformation, and storage operations.
    """
    def __init__(self, db: StockDatabase):
        self.db = db
        self.fmp_fetcher = FMPFetcher()
        self.analysis_processor = AnalysisProcessor(self.fmp_fetcher)
        conn = self.db._get_connection()
        
        # Initialize all required store objects
        self.store_core = StoreCore(conn)
        self.store_market_data = StoreMarketData(conn)
        self.store_valuation = StoreValuation(conn)
        self.store_financial_metrics = StoreFinancialMetrics(conn)
        self.store_growth = StoreGrowth(conn)
        self.store_analysis = StoreAnalysis(conn)
        self.store_corporate_actions = StoreCorporateActions(conn)
        self.store_analysis_data = StoreAnalysisData(conn)
        self.store_macro = StoreMacro(conn)
        
        logging.basicConfig(level=logging.INFO)

    def populate(self, tickers: Optional[List[str]] = None):
        """
        Populate the database with data for the specified tickers.
        If no tickers are provided, uses S&P 500 tickers.
        """
        if tickers is None:
            tickers = self.fmp_fetcher.get_sp500_tickers()
            logging.info(f"Using default tickers from S&P 500 ({len(tickers)} tickers)")
        else:
            logging.info(f"Populating data for provided tickers: {tickers}")

        self.populate_batch(tickers)

    def populate_batch(self, tickers: List[str]):
        """
        Process a batch of tickers sequentially.
        """
        for ticker in tickers:
            logging.info(f"Starting population for ticker: {ticker}")
            self.populate_one_ticker(ticker)
    
    def populate_one_ticker(self, ticker: str):
        """
        Populate data for a single ticker, processing one table at a time.
        """
        try:
            ## Process each data type separately
            #self.populate_analyst_estimates(ticker, None)
            #self.populate_ratings(ticker, None)

            logging.info(f"Successfully populated data for ticker: {ticker}")
        except Exception as e:
            logging.error(f"Failed to populate {ticker}: {e}")
    
    #region Populate Tables
    def _populate_table(
        self,
        ticker: str,
        date: Optional[str],
        processor_fn: Callable[[str, Optional[str], Optional[str]], Optional[List[Dict[str, Any]]]],
        store_fn: Callable[[Dict[str, Any]], None],
        label: str
    ):
        """Generic processor + store pipeline"""
        try:
            records = processor_fn(ticker, date)
            if records:
                logging.info(f"Processing {len(records)} {label} records for {ticker}")
                for record in records:
                    data = {
                        'symbol': ticker,
                        'date': record['date'],
                        **record
                    }
                    logging.debug(f"Storing {label} data: {data}")
                    store_fn(data)
                logging.info(f"Successfully stored {len(records)} {label} records for {ticker}")
            else:
                logging.warning(f"No {label} data available for {ticker}")
        except Exception as e:
            logging.error(f"Failed to process {label} for {ticker}: {e}")
            logging.exception("Full traceback:")

    def populate_analyst_estimates(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.analysis_processor.process_analyst_estimates,
            store_fn=self.store_analysis.store_analyst_estimates,
            label="analyst estimates"
        )

    def populate_ratings(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.analysis_processor.process_ratings,
            store_fn=self.store_analysis.store_ratings,
            label="ratings"
        )


    #endregion
