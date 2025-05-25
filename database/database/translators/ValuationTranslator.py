from typing import Dict, Any, List
from .utils import safe_float, safe_int

class ValuationTranslator:
    @staticmethod
    def translate_enterprise_values(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates enterprise values data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw enterprise values data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated enterprise values data in the database schema format
        """
        if not data:
            return []
        
        translated_values = []
        for value in data:
            translated = {
                'symbol': value.get('symbol'),
                'date': value.get('date'),
                'enterprise_value': safe_float(value.get('enterpriseValue')),
                'add_total_debt': safe_float(value.get('addTotalDebt')),
                'minus_cash_and_cash_equivalents': safe_float(value.get('minusCashAndCashEquivalents')),
                'number_of_shares': safe_int(value.get('numberOfShares')),
            }
            translated_values.append(translated)
        
        return translated_values

    @staticmethod
    def translate_owner_earnings(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates owner earnings data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw owner earnings data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated owner earnings data in the database schema format
        """
        if not data:
            return []
        
        translated_earnings = []
        for earnings in data:
            translated = {
                'symbol': earnings.get('symbol'),
                'date': earnings.get('date'),
                'period': earnings.get('period'),
                'fiscal_year': earnings.get('fiscalYear'),
                'avg_ppe': safe_float(earnings.get('averagePPE')),
                'growth_capex': safe_float(earnings.get('growthCapex')),
                'maintenance_capex': safe_float(earnings.get('maintenanceCapex')),
                'owners_earnings': safe_float(earnings.get('ownersEarnings')),
                'owners_earnings_per_share': safe_float(earnings.get('ownersEarningsPerShare')),
            }
            translated_earnings.append(translated)
        
        return translated_earnings

    @staticmethod
    def translate_levered_discounted_cash_flow(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates levered discounted cash flow data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw levered discounted cash flow data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated levered discounted cash flow data in the database schema format
        """
        if not data:
            return []

        translated_dcf = []
        for dcf in data:
            translated = {
                'symbol': dcf.get('symbol'),
                'date': dcf.get('date'),
                'dcf': safe_float(dcf.get('dcf')),
            }
            translated_dcf.append(translated)
        
        return translated_dcf

    @staticmethod
    def translate_discounted_cash_flow(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates discounted cash flow data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw discounted cash flow data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated discounted cash flow data in the database schema format
        """
        if not data:
            return []
        
        translated_dcf = []
        for dcf in data:
            translated = {
                'symbol': dcf.get('symbol'),
                'date': dcf.get('date'),
                'dcf': safe_float(dcf.get('dcf'))
            }
            translated_dcf.append(translated)
        
        return translated_dcf 