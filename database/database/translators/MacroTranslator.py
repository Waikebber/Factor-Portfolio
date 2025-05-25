from typing import Dict, Any, List
from .utils import safe_float, safe_int

class MacroTranslator:
    @staticmethod
    def translate_economic_indicators(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates economic indicators data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw economic indicators data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated economic indicators data in the database schema format
        """
        if not data:
            return []
        translated_indicators = []
        for indicator in data:
            translated = {
                'name': indicator.get('name'),
                'date': indicator.get('date'),
                'value': indicator.get('value')
            }
            translated_indicators.append(translated)
        
        return translated_indicators

    @staticmethod
    def translate_industry_pe(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates industry PE data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw industry PE data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated industry PE data in the database schema format
        """
        if not data:
            return []
        
        translated_pe = []
        for pe in data:
            translated = {
                'date': pe.get('date'),
                'industry': pe.get('industry'),
                'exchange': pe.get('exchange'),
                'pe': float(pe.get('pe')) if pe.get('pe') is not None else None,
            }
            translated_pe.append(translated)
        
        return translated_pe

    @staticmethod
    def translate_sector_pe(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates sector PE data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw sector PE data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated sector PE data in the database schema format
        """
        if not data:
            return []
        
        translated_pe = []
        for pe in data:
            translated = {
                'date': pe.get('date'),
                'sector': pe.get('sector'),
                'exchange': pe.get('exchange'),
                'pe': float(pe.get('pe')) if pe.get('pe') is not None else None,
            }
            translated_pe.append(translated)
        
        return translated_pe

    @staticmethod
    def translate_industry_performance(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates industry performance data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw industry performance data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated industry performance data in the database schema format
        """
        if not data:
            return []
        
        translated_performance = []
        for performance in data:
            translated = {
                'date': performance.get('date'),
                'industry': performance.get('industry'),
                'exchange': performance.get('exchange'),
                'average_change': float(performance.get('averageChange')) if performance.get('averageChange') is not None else None,
            }
            translated_performance.append(translated)
        
        return translated_performance

    @staticmethod
    def translate_sector_performance(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates sector performance data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw sector performance data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated sector performance data in the database schema format
        """
        if not data:
            return []
        
        translated_performance = []
        for performance in data:
            translated = {
                'date': performance.get('date'),
                'sector': performance.get('sector'),
                'exchange': performance.get('exchange'),
                'average_change': float(performance.get('averageChange')) if performance.get('averageChange') is not None else None,
            }
            translated_performance.append(translated)
        
        return translated_performance

    @staticmethod
    def translate_treasury_rates(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates treasury rates data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw treasury rates data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated treasury rates data in the database schema format
        """
        if not data:
            return []
        translated_rates = []
        for rate in data:
            translated = {
                'symbol': rate.get('symbol'),
                'date': rate.get('date'),
                'month_1': safe_float(rate.get('month1')),
                'month_2': safe_float(rate.get('month2')),
                'month_3': safe_float(rate.get('month3')),
                'month_6': safe_float(rate.get('month6')),
                'year_1': safe_float(rate.get('year1')),
                'year_2': safe_float(rate.get('year2')),
                'year_3': safe_float(rate.get('year3')),
                'year_5': safe_float(rate.get('year5')),
                'year_7': safe_float(rate.get('year7')),
                'year_10': safe_float(rate.get('year10')),
                'year_20': safe_float(rate.get('year20')),
                'year_30': safe_float(rate.get('year30')),
            }
            translated_rates.append(translated)
        return translated_rates 
    
    @staticmethod
    def translate_mergers_acquisitions(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates mergers and acquisitions data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw mergers and acquisitions data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated mergers and acquisitions data in the database schema format
        """
        if not data:
            return []
        
        translated_ma = []

        for ma in data:
            translated = {
                'symbol': ma.get('symbol'),  # Acquiring company
                'targeted_symbol': ma.get('targetedSymbol'),  # Acquired company
                'transaction_date': ma.get('transactionDate'),
            }
            translated_ma.append(translated)
        
        return translated_ma