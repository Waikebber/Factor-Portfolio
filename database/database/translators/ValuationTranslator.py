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
                'market_cap': safe_float(value.get('marketCap')),
                'total_debt': safe_float(value.get('totalDebt')),
                'cash_and_equivalents': safe_float(value.get('cashAndEquivalents')),
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
                'net_income': safe_float(earnings.get('netIncome')),
                'depreciation_and_amortization': safe_float(earnings.get('depreciationAndAmortization')),
                'capital_expenditure': safe_float(earnings.get('capitalExpenditure')),
                'working_capital_change': safe_float(earnings.get('workingCapitalChange')),
                'owner_earnings': safe_float(earnings.get('ownerEarnings')),
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
                'stock_price': safe_float(dcf.get('stockPrice')),
                'dcf_difference': safe_float(dcf.get('dcfDifference')),
                'dcf_difference_percent': safe_float(dcf.get('dcfDifferencePercent')),
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
                'dcf': safe_float(dcf.get('dcf')),
                'stock_price': safe_float(dcf.get('stockPrice')),
                'dcf_difference': safe_float(dcf.get('dcfDifference')),
                'dcf_difference_percent': safe_float(dcf.get('dcfDifferencePercent')),
            }
            translated_dcf.append(translated)
        
        return translated_dcf 