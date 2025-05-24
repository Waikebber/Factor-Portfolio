from abc import ABC, abstractmethod
from typing import Dict, Any, Union, List, Optional
import pandas as pd
from datetime import datetime

class FinancialDataEndpoint(ABC):
    """Base class for financial data endpoints.
    
    This abstract base class defines the interface for financial data endpoints.
    All concrete endpoint implementations should inherit from this class and
    implement the required methods.
    """
    
    @abstractmethod
    def fetch(self, ticker: str) -> Dict[str, Any]:
        """Fetch a complete set of fundamental data for a single ticker.
        
        Args:
            ticker: The stock ticker symbol to fetch data for.
            
        Returns:
            A dictionary containing the fundamental data for the ticker.
        """
        pass
    
    @abstractmethod
    def get_json(self, url: str, retries: int = 3) -> Any:
        """Make an HTTP GET request and return the JSON response.
        
        Args:
            url: The URL to make the request to.
            retries: Number of retry attempts if the request fails.
            
        Returns:
            The JSON response data.
        """
        pass
    
    def _process_response(self, data: Any) -> Dict[str, Any]:
        """Process and validate the API response data.
        
        Args:
            data: The raw response data from the API.
            
        Returns:
            Processed and validated data in dictionary format.
        """
        if not data:
            return {}
        if isinstance(data, list):
            return data[0] if data and isinstance(data[0], dict) else {}
        if isinstance(data, dict):
            return data
        return {}
    
    def _format_date(self, date: Optional[Union[str, datetime]]) -> Optional[str]:
        """Format a date into the standard format expected by the API.
        
        Args:
            date: The date to format, either as a string or datetime object.
            
        Returns:
            Formatted date string or None if no date provided.
        """
        if not date:
            return None
        if isinstance(date, datetime):
            return date.strftime("%Y-%m-%d")
        return date
