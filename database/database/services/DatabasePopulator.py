from datetime import datetime, timedelta
import logging
import pandas as pd
from typing import Dict, Any, Optional, List, Callable, Union
from ..StockDatabase import StockDatabase
from ..db_writers import *
from ..processing import *
from ..data_fetchers.FMPFetcher import FMPFetcher

class DatabasePopulator:
    """
    Service class responsible for orchestrating the database population process.
    Coordinates data fetching, transformation, and storage operations.
    """
    def __init__(self, db: StockDatabase):
        self.db = db
        self.fmp_fetcher = FMPFetcher()
        conn = self.db._get_connection()

        # Processors
        self.analysis_processor = AnalysisProcessor(self.fmp_fetcher)
        self.analyst_data_processor = AnalystDataProcessor(self.fmp_fetcher)
        self.valuation_processor = ValuationProcessor(self.fmp_fetcher)
        self.financial_metrics_processor = FinancialMetricsProcessor(self.fmp_fetcher)
        self.growth_processor = GrowthProcessor(self.fmp_fetcher)
        self.core_processor = CoreProcessor(self.fmp_fetcher)
        
        # Initialize all required store objects
        self.store_core = StoreCore(conn)
        self.store_market_data = StoreMarketData(conn)
        self.store_valuation = StoreValuation(conn)
        self.store_financial_metrics = StoreFinancialMetrics(conn)
        self.store_growth = StoreGrowth(conn)
        self.store_analysis = StoreAnalysis(conn)
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
            self.populate_analysis_data(ticker, None)
            self.populate_analyst_data(ticker, None)
            self.populate_core(ticker, None)
            self.populate_financial_metrics(ticker, None)
            self.populate_growth(ticker, None)


            logging.info(f"Successfully populated data for ticker: {ticker}")
        except Exception as e:
            logging.error(f"Failed to populate {ticker}: {e}")
    
    #region Populate Data Table Sets
    
    def populate_analysis_data(self, ticker: str, date: Optional[str]):
        self.populate_analyst_estimates(ticker, date)
        self.populate_ratings(ticker, date)
    
    def populate_analyst_data(self, ticker: str, date: Optional[str]):
        self.populate_grades(ticker, date)
        self.populate_grades_consensus(ticker, date)
        self.populate_price_target_consensus(ticker, date)
        self.populate_price_target_summary(ticker, date)
    
    def populate_core(self, ticker: str, date: Optional[str]):
        self.populate_stocks(ticker, date)
        self.populate_employee_count(ticker, date)
    
    def populate_financial_metrics(self, ticker: str, date: Optional[str]):
        self.populate_key_metrics(ticker, date)
        self.populate_financial_ratios(ticker, date)
        self.populate_earnings(ticker, date)
    
    def populate_growth(self, ticker: str, date: Optional[str]):
        self.populate_financial_statement_growth(ticker, date)
        self.populate_cashflow_statement_growth(ticker, date)
        self.populate_balance_sheet_growth(ticker, date)
        self.populate_income_statement_growth(ticker, date)
    

    #endregion
        
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
                    if not isinstance(record, dict):
                        logging.warning(f"Skipping non-dictionary record for {ticker}: {record}")
                        continue
                        
                    data = {
                        'symbol': ticker,
                        **record
                    }
                    # Only add date if it exists in the record
                    if 'date' in record:
                        data['date'] = record['date']
                        
                    logging.debug(f"Storing {label} data: {data}")
                    store_fn(data)
                logging.info(f"Successfully stored {len(records)} {label} records for {ticker}")
            else:
                logging.warning(f"No {label} data available for {ticker}")
        except Exception as e:
            logging.error(f"Failed to process {label} for {ticker}: {e}")
            logging.exception("Full traceback:")

    #region Analysis
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
    
    #region Analyst Data
    def populate_grades(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.analyst_data_processor.process_grades,
            store_fn=self.store_analysis_data.store_grades,
            label="grades"
        )

    def populate_grades_consensus(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.analyst_data_processor.process_grades_consensus,
            store_fn=self.store_analysis_data.store_grades_consensus,
            label="grades consensus"
        )

    def populate_price_target_consensus(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.analyst_data_processor.process_price_target_consensus,
            store_fn=self.store_analysis_data.store_price_target_consensus,
            label="price target consensus"
        )

    def populate_price_target_summary(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.analyst_data_processor.process_price_target_summary,
            store_fn=self.store_analysis_data.store_price_target_summary,
            label="price target summary"
        )
    #endregion
    
    #region Core
    def populate_stocks(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.core_processor.process_stocks,
            store_fn=self.store_core.store_stock,
            label="stock metadata"
        )

    def populate_employee_count(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.core_processor.process_employee_count,
            store_fn=self.store_core.store_employee_count,
            label="employee count"
        )
    #endregion
    
    #region Financial Metrics
    def populate_key_metrics(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.financial_metrics_processor.process_key_metrics,
            store_fn=self.store_financial_metrics.store_key_metrics,
            label="key metrics"
        )
    
    def populate_financial_ratios(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.financial_metrics_processor.process_financial_ratios,
            store_fn=self.store_financial_metrics.store_financial_ratios,
            label="key financial ratios"
        )

    def populate_earnings(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.financial_metrics_processor.process_earnings,
            store_fn=self.store_financial_metrics.store_earnings,
            label="earnings"
        )
    #endregion

    #region Growth
    def populate_financial_statement_growth(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.growth_processor.process_financial_statement_growth,
            store_fn=self.store_growth.store_financial_statement_growth,
            label="financial statement growth"
        )

    def populate_cashflow_statement_growth(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.growth_processor.process_cashflow_statement_growth,
            store_fn=self.store_growth.store_cashflow_statement_growth,
            label="cashflow statement growth"
        )

    def populate_balance_sheet_growth(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.growth_processor.process_balance_sheet_growth,
            store_fn=self.store_growth.store_balance_sheet_growth,
            label="balance sheet growth"
        )

    def populate_income_statement_growth(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.growth_processor.process_income_statement_growth,
            store_fn=self.store_growth.store_income_statement_growth,
            label="income statement growth"
        )
    #endregion

    #region Market Data
    #endregion

    #region Valuation
    #endregion

    #region Macro
    #endregion

    #endregion
