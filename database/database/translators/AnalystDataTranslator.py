from typing import Dict, Any, List, Union
from datetime import datetime
from .utils import safe_float, safe_int

class AnalystDataTranslator:
    @staticmethod
    def translate_grades(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates grades data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw grades data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated grades data in the database schema format
        """
        if not data:
            return []
        
        translated_grades = []
        for grade in data:
            translated = {
                'symbol': grade.get('symbol'),
                'date': grade.get('date'),
                'buy': safe_int(grade.get('analystRatingsBuy')),
                'hold': safe_int(grade.get('analystRatingsHold')),
                'sell': safe_int(grade.get('analystRatingsSell')),
                'strong_sell': safe_int(grade.get('analystRatingsStrongSell'))
            }
            translated_grades.append(translated)
        
        return translated_grades

    @staticmethod
    def translate_grades_consensus(data: Union[Dict[str, Any], List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
        """
        Translates grades consensus data from the API response format to the database schema.
        
        Args:
            data (Union[Dict[str, Any], List[Dict[str, Any]]]): Raw grades consensus data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated grades consensus data in the database schema format
        """
        if not data:
            return []
        
        # Handle single dictionary response
        if isinstance(data, dict):
            data = [data]

        current_date = datetime.now().strftime('%Y-%m-%d')
        translated_consensus = []
        for consensus in data:
            translated = {
                'symbol': consensus.get('symbol'),
                'date': current_date,
                'strong_buy': safe_int(consensus.get('strong_buy')),
                'buy': safe_int(consensus.get('buy')),
                'hold': safe_int(consensus.get('hold')),
                'sell': safe_int(consensus.get('sell')),
                'strong_sell': safe_int(consensus.get('strong_sell')),
                'consensus': consensus.get('consensus')
            }
            translated_consensus.append(translated)
        
        return translated_consensus

    @staticmethod
    def translate_price_target_consensus(data: Union[Dict[str, Any], List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
        """
        Translates price target consensus data from the API response format to the database schema.
        
        Args:
            data (Union[Dict[str, Any], List[Dict[str, Any]]]): Raw price target consensus data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated price target consensus data in the database schema format
        """
        if not data:
            return []
        
        # Handle single dictionary response
        if isinstance(data, dict):
            data = [data]
        
        current_date = datetime.now().strftime('%Y-%m-%d')
        translated_consensus = []
        for consensus in data:
            translated = {
                'symbol': consensus.get('symbol'),
                'date': current_date,
                'target_high': safe_float(consensus.get('target_high')),
                'target_low': safe_float(consensus.get('target_low')),
                'target_consensus': safe_float(consensus.get('target_consensus')),
                'target_median': safe_float(consensus.get('target_median'))
            }
            translated_consensus.append(translated)
        
        return translated_consensus

    @staticmethod
    def translate_price_target_summary(data: Union[Dict[str, Any], List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
        """
        Translates price target summary data from the API response format to the database schema.
        
        Args:
            data (Union[Dict[str, Any], List[Dict[str, Any]]]): Raw price target summary data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated price target summary data in the database schema format
        """
        if not data:
            return []
        
        # Handle single dictionary response
        if isinstance(data, dict):
            data = [data]

        translated_summary = []
        for summary in data:
            translated = {
                'symbol': summary.get('symbol'),
                'last_month_count': safe_int(summary.get('last_month_count')),
                'last_month_avg_price_target': safe_float(summary.get('last_month_avg_price_target')),
                'last_quarter_count': safe_int(summary.get('last_quarter_count')),
                'last_quarter_avg_price_target': safe_float(summary.get('last_quarter_avg_price_target')),
                'last_year_count': safe_int(summary.get('last_year_count')),
                'last_year_avg_price_target': safe_float(summary.get('last_year_avg_price_target')),
                'all_time_count': safe_int(summary.get('all_time_count')),
                'all_time_avg_price_target': safe_float(summary.get('all_time_avg_price_target'))
            }
            translated_summary.append(translated)
        
        return translated_summary 