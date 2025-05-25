from datetime import datetime, timedelta
from typing import Dict, Any
from dataclasses import dataclass, field
from pathlib import Path
import json

@dataclass
class DataFetchConfig:
    """Configuration for data fetching parameters"""
    # General settings
    max_retries: int = 3
    retry_delay: int = 30
    batch_size: int = 25
    batch_delay: int = 60

    # 5 years ago
    general_start_date: str = (datetime.now() - timedelta(days=5*365)).strftime('%Y-%m-%d')

    general: Dict[str, Any] = field(default_factory=lambda: {})

    ################### Analysis and Analyst Data ###################
    analyst_estimates: Dict[str, Any] = field(default_factory=lambda: {
        'period': 'annual',
        'page': 0,
        'limit': 10
    })

    ratings: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 10
    })

    grades: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 100
    })

    ################### Core ###################
    employee_count: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 50
    })

    ################### Market Data ###################
    prices: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 1000
    })

    dividend_adjusted_prices: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 1000
    })

    dividends: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 10
    })

    splits: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 10
    })

    market_cap: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 10
    })

    share_float: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 1
    })

    ################### Valuation ###################
    discounted_cash_flow: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 1
    })

    levered_discounted_cash_flow: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 1
    })

    enterprise_values: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 10,
        'period': 'annual'
    })

    owner_earnings: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 10
    })

    ################### Financial Metrics ###################
    key_metrics: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 20,
        'period': 'annual'
    })

    financial_ratios: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 20,
        'period': 'annual'
    })

    earnings: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 75
    })

    ################### Growth ###################
    financial_statement_growth: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 20,
        'period': 'annual'
    })

    income_statement_growth: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 20,
        'period': 'annual'
    })

    balance_sheet_growth: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 20,
        'period': 'annual'
    })

    cashflow_statement_growth: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 20,
        'period': 'annual'
    })

    ################### Macro ###################
    mergers_acquisitions: Dict[str, Any] = field(default_factory=lambda: {
        'page': 0,
        'limit': 100
    })

    economic_indicators: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 1000
    })

    industry_pe: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 1000,
        'exchange': 'NYSE'
    })

    sector_pe: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 1000,
        'exchange': 'NYSE'
    })

    industry_performance: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 1000,
        'exchange': 'NYSE'
    })

    sector_performance: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 1000,
        'exchange': 'NYSE'
    })

    treasury_rates: Dict[str, Any] = field(default_factory=lambda: {
        'limit': 1000
    })

    @classmethod
    def from_file(cls, config_path: str = None) -> 'DataFetchConfig':
        """Load configuration from a JSON file"""
        if config_path is None:
            config_path = str(Path(__file__).parent / 'data_fetch_config.json')
        
        try:
            with open(config_path, 'r') as f:
                config_data = json.load(f)
            return cls(**config_data)
        except FileNotFoundError:
            # If config file doesn't exist, create it with default values
            config = cls()
            config.save_to_file(config_path)
            return config

    def save_to_file(self, config_path: str = None) -> None:
        """Save current configuration to a JSON file"""
        if config_path is None:
            config_path = str(Path(__file__).parent / 'data_fetch_config.json')
        
        config_data = {
            'general': self.general,
            'max_retries': self.max_retries,
            'retry_delay': self.retry_delay,
            'batch_size': self.batch_size,
            'batch_delay': self.batch_delay,
            'general_start_date': self.general_start_date,
            'analyst_estimates': self.analyst_estimates,
            'ratings': self.ratings,
            'grades': self.grades,
            'earnings': self.earnings,
            'mergers_acquisitions': self.mergers_acquisitions,
            'prices': self.prices,
            'dividend_adjusted_prices': self.dividend_adjusted_prices,
            'dividends': self.dividends,
            'splits': self.splits,
            'market_cap': self.market_cap,
            'share_float': self.share_float,
            'discounted_cash_flow': self.discounted_cash_flow,
            'levered_discounted_cash_flow': self.levered_discounted_cash_flow,
            'enterprise_values': self.enterprise_values,
            'owner_earnings': self.owner_earnings,
            'key_metrics': self.key_metrics,
            'financial_ratios': self.financial_ratios,
            'stock_metrics': self.stock_metrics,
            'financial_statement_growth': self.financial_statement_growth,
            'income_statement_growth': self.income_statement_growth,
            'balance_sheet_growth': self.balance_sheet_growth,
            'cashflow_statement_growth': self.cashflow_statement_growth,
            'economic_indicators': self.economic_indicators,
            'industry_pe': self.industry_pe,
            'sector_pe': self.sector_pe,
            'industry_performance': self.industry_performance,
            'sector_performance': self.sector_performance,
            'treasury_rates': self.treasury_rates
        }
        
        with open(config_path, 'w') as f:
            json.dump(config_data, f, indent=4)

    def update_config(self, **kwargs) -> None:
        """Update configuration parameters"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value) 