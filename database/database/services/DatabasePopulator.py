from datetime import datetime, timedelta
import logging
import pandas as pd
from typing import Dict, Any, Optional, List, Callable, Union
from ..StockDatabase import StockDatabase
from ..db_writers import *
from ..processing import *
from ..data_fetchers.FMPFetcher import FMPFetcher
from ..data_fetchers.WikiFetcher import WikiFetcher
from tqdm import tqdm
import os

# Configure logging to write to a file
log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'logs')
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, 'database_population.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

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
        self.market_data_processor = MarketDataProcessor(self.fmp_fetcher)
        self.macro_processor = MacroProcessor(self.fmp_fetcher)

        # Initialize all required store objects
        self.store_core = StoreCore(conn)
        self.store_market_data = StoreMarketData(conn)
        self.store_valuation = StoreValuation(conn)
        self.store_financial_metrics = StoreFinancialMetrics(conn)
        self.store_growth = StoreGrowth(conn)
        self.store_analysis = StoreAnalysis(conn)
        self.store_analysis_data = StoreAnalysisData(conn)
        self.store_macro = StoreMacro(conn)

    def set_up_database(self):
        """Initialize the database with macro data using a progress bar."""
        # Define macro operations
        macro_operations = [
            (self.populate_mergers_and_acquisitions, "Mergers & Acquisitions"),
            (self.populate_treasury_rates, "Treasury Rates"),
            (self.populate_industry_pe, "Industry PE"),
            (self.populate_sector_pe, "Sector PE"),
            (self.populate_industry_performance, "Industry Performance"),
            (self.populate_sector_performance, "Sector Performance"),
            (self.populate_economic_indicators, "Economic Indicators")
        ]

        # Disable logging output during progress bar display
        logging.getLogger().setLevel(logging.ERROR)
        
        try:
            with tqdm(total=len(macro_operations), desc="Initializing Database", position=0) as pbar:
                for operation, label in macro_operations:
                    try:
                        operation(None)
                        logging.info(f"Successfully processed {label}")
                    except Exception as e:
                        logging.error(f"Failed to process {label}: {e}")
                    finally:
                        pbar.update(1)
                        pbar.set_description(f"Initializing Database - {label}")
        finally:
            logging.getLogger().setLevel(logging.INFO)

    def populate_sp500(self):
        """Populate the database with S&P 500 data."""
        wiki_fetcher = WikiFetcher()
        tickers = wiki_fetcher.get_sp500_tickers()
        self.populate_batch(tickers)

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
        Process a batch of tickers sequentially with progress bar.
        """
        operations = [
            (self.populate_core, "Core Data"),
            (self.populate_analysis_data, "Analysis Data"),
            (self.populate_analyst_data, "Analyst Data"),
            (self.populate_financial_metrics, "Financial Metrics"),
            (self.populate_growth, "Growth Data"),
            (self.populate_market_data, "Market Data"),
            (self.populate_valuation, "Valuation Data")
        ]

        # Store original logging level
        original_level = logging.getLogger().getEffectiveLevel()
        logging.getLogger().setLevel(logging.ERROR)
        
        ticker_errors = {}
        try:
            description = "Overall Progress"
            with tqdm(total=len(tickers), desc=description, position=0, leave=False, colour="green") as ticker_pbar:
                for ticker in tickers:
                    ticker_errors[ticker] = []
                    for operation, label in operations:
                        try:
                            ticker_pbar.set_description(f"{description} - {ticker} - {label}")
                            operation(ticker, None)
                            logging.info(f"Successfully processed {label} for {ticker}")
                        except Exception as e:
                            error_msg = f"Failed to process {label}: {str(e)}"
                            ticker_errors[ticker].append(error_msg)
                    ticker_pbar.update(1)

            # Errors
            for ticker, errors in ticker_errors.items():
                if errors:
                    logging.error(f"\nErrors for {ticker}:")
                    for error in errors:
                        logging.error(f"  - {error}")

        finally:
            # Restore original logging level
            logging.getLogger().setLevel(original_level)

    #region Populate Functions
    #region Populate Groups
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
    
    def populate_market_data(self, ticker: str, date: Optional[str]):
        self.populate_dividends(ticker, date)
        self.populate_dividend_adjusted_prices(ticker, date)
        self.populate_market_cap(ticker, date)
        self.populate_share_float(ticker, date)
        self.populate_splits(ticker, date)
        self.populate_price(ticker, date)

    def populate_valuation(self, ticker: str, date: Optional[str]):
        self.populate_discounted_cash_flow(ticker, date)
        self.populate_levered_discounted_cash_flow(ticker, date)
        self.populate_owner_earnings(ticker, date)
        self.populate_enterprise_values(ticker, date)

    def populate_macro(self, date: Optional[str]):
        self.populate_mergers_and_acquisitions(date)
        self.populate_treasury_rates(date)
        self.populate_industry_pe(date)
        self.populate_sector_pe(date)
        self.populate_industry_performance(date)
        self.populate_sector_performance(date)
        self.populate_economic_indicators(date)
    #endregion

    #region Populate Templates
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

    def _populate_macro_table(
        self,
        date: Optional[str],
        processor_fn: Callable[[Optional[str]], Optional[List[Dict[str, Any]]]],
        store_fn: Callable[[Dict[str, Any]], None],
        label: str
    ):
        """Generic processor + store pipeline for macro (non-ticker) data."""
        try:
            records = processor_fn(date)
            if records:
                logging.info(f"Processing {len(records)} {label} macro records")
                for record in records:
                    if not isinstance(record, dict):
                        logging.warning(f"Skipping non-dictionary macro record: {record}")
                        continue

                    # Only add date if it exists in the record
                    data = {**record}
                    if 'date' in record:
                        data['date'] = record['date']

                    logging.debug(f"Storing {label} macro data: {data}")
                    store_fn(data)
                logging.info(f"Successfully stored {len(records)} {label} macro records")
            else:
                logging.warning(f"No {label} macro data available")
        except Exception as e:
            logging.error(f"Failed to process macro {label}: {e}")
            logging.exception("Full traceback:")
    #endregion

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
    def populate_dividends(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.market_data_processor.process_dividends,
            store_fn=self.store_market_data.store_dividend,
            label="dividends"
        )

    def populate_dividend_adjusted_prices(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.market_data_processor.process_dividend_adjusted_prices,
            store_fn=self.store_market_data.store_dividend_adjusted_price,
            label="dividend adjusted prices"
        )

    def populate_price(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.market_data_processor.process_prices,
            store_fn=self.store_market_data.store_price,
            label="price"
        )

    def populate_market_cap(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.market_data_processor.process_market_cap,
            store_fn=self.store_market_data.store_market_cap,
            label="market cap"
        )

    def populate_share_float(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.market_data_processor.process_share_float,
            store_fn=self.store_market_data.store_share_float,
            label="share float"
        )

    def populate_splits(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.market_data_processor.process_splits,
            store_fn=self.store_market_data.store_split,
            label="splits"
        )

    #endregion

    #region Valuation
    def populate_discounted_cash_flow(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.valuation_processor.process_discounted_cash_flow,
            store_fn=self.store_valuation.store_discounted_cash_flow,
            label="discounted cash flow"
        )

    def populate_levered_discounted_cash_flow(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.valuation_processor.process_levered_discounted_cash_flow,
            store_fn=self.store_valuation.store_levered_discounted_cash_flow,
            label="levered discounted cash flow"
        )

    def populate_owner_earnings(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.valuation_processor.process_owner_earnings,
            store_fn=self.store_valuation.store_owner_earnings,
            label="owner earnings"
        )

    def populate_enterprise_values(self, ticker: str, date: Optional[str]):
        self._populate_table(
            ticker=ticker,
            date=date,
            processor_fn=self.valuation_processor.process_enterprise_values,
            store_fn=self.store_valuation.store_enterprise_values,
            label="enterprise values"
        )
    #endregion

    #region Macro
    def populate_mergers_and_acquisitions(self, date: Optional[str]):
        self._populate_macro_table(
            date=date,
            processor_fn=self.macro_processor.process_mergers_acquisitions,
            store_fn=self.store_macro.store_mergers_and_acquisitions,
            label="mergers and acquisitions"
        )

    def populate_industry_pe(self, date: Optional[str]):
        self._populate_macro_table(
            date=date,
            processor_fn=self.macro_processor.process_industry_pe,
            store_fn=self.store_macro.store_industry_pe,
            label="industry pe"
        )
    
    def populate_sector_pe(self, date: Optional[str]):
        self._populate_macro_table(
            date=date,
            processor_fn=self.macro_processor.process_sector_pe,
            store_fn=self.store_macro.store_sector_pe,
            label="sector pe"
        )
    
    def populate_industry_performance(self, date: Optional[str]):
        self._populate_macro_table(
            date=date,
            processor_fn=self.macro_processor.process_industry_performance,
            store_fn=self.store_macro.store_industry_performance,
            label="industry performance"
        )
    
    def populate_sector_performance(self, date: Optional[str]):
        self._populate_macro_table(
            date=date,
            processor_fn=self.macro_processor.process_sector_performance,
            store_fn=self.store_macro.store_sector_performance,
            label="sector performance"
        )
    
    def populate_treasury_rates(self, date: Optional[str]):
        self._populate_macro_table(
            date=date,
            processor_fn=self.macro_processor.process_treasury_rates,
            store_fn=self.store_macro.store_treasury_rates,
            label="treasury rates"
        )
    
    def populate_economic_indicators(self, date: Optional[str]):
        self._populate_macro_table(
            date=date,
            processor_fn=self.macro_processor.process_economic_indicators,
            store_fn=self.store_macro.store_economic_indicators,
            label="economic indicators"
        )  

    #endregion
    #endregion