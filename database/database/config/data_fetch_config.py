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

    # Date ranges for different data types
    analyst_estimates: Dict[str, Any] = field(default_factory=lambda: {
        'start_date': None,
        'end_date': None,
        'period': 'annual',
        'page': 0,
        'limit': 10
    })

    ratings: Dict[str, Any] = field(default_factory=lambda: {
        'start_date': None,
        'end_date': None,
        'limit': 10
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
            'max_retries': self.max_retries,
            'retry_delay': self.retry_delay,
            'batch_size': self.batch_size,
            'batch_delay': self.batch_delay,
            'analyst_estimates': self.analyst_estimates,
            'price_data': self.price_data,
            'fundamental_data': self.fundamental_data,
            'economic_indicators': self.economic_indicators
        }
        
        with open(config_path, 'w') as f:
            json.dump(config_data, f, indent=4)

    def update_config(self, **kwargs) -> None:
        """Update configuration parameters"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value) 