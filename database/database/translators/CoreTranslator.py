from typing import Dict, Any, List, Optional, Union
from datetime import datetime

class CoreTranslator:
    @staticmethod
    def translate_stocks(data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Translate stock data from API format to database schema format."""
        if not isinstance(data, dict):
            return []

        record = {
            'symbol': data.get('symbol'),
            'company_name': data.get('company_name'),
            'exchange_short_name': data.get('exchange_short_name'),
            'industry': data.get('industry'),
            'sector': data.get('sector'),
            'country': data.get('country'),
            'is_actively_trading': data.get('is_actively_trading'),
        }
        if record['symbol']:
            return [record]
        return []

    @staticmethod
    def translate_employee_count(data: Union[Dict[str, Any], List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
        """Translate employee count data from API format to database schema format.
        
        Args:
            data: Either a single dictionary or a list of dictionaries containing employee count data
            
        Returns:
            List of dictionaries in the database schema format
        """
        if isinstance(data, dict):
            data = [data]
        elif not isinstance(data, list):
            return []
            
        translated_records = []
        for record in data:
            if not isinstance(record, dict):
                continue
                
            translated = {
                'symbol': record.get('symbol'),
                'date': record.get('date'),
                'employee_count': record.get('employeeCount')
            }
            if all(v is not None for v in translated.values()):
                translated_records.append(translated)
                
        return translated_records
