from typing import Dict, Any, List
from .utils import safe_float, safe_int

class MarketDataTranslator:
    @staticmethod
    def translate_share_float(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates share float data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw share float data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated share float data in the database schema format
        """
        if not data:
            return []
        
        translated_float = []
        for float_data in data:
            translated = {
                'symbol': float_data.get('symbol'),
                'date': float_data.get('date'),
                'free_float': safe_float(float_data.get('freeFloat')),
                'float_shares': safe_int(float_data.get('floatShares')),
                'outstanding_shares': safe_int(float_data.get('outstandingShares')),
            }
            translated_float.append(translated)
        
        return translated_float

    @staticmethod
    def translate_market_cap(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates market cap data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw market cap data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated market cap data in the database schema format
        """
        if not data:
            return []
        
        translated_cap = []
        for cap in data:
            translated = {
                'symbol': cap.get('symbol'),
                'date': cap.get('date'),
                'market_cap': float(cap.get('marketCap')) if cap.get('marketCap') is not None else None,
            }
            translated_cap.append(translated)
        
        return translated_cap

    @staticmethod
    def translate_dividend_adjusted_price_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates dividend adjusted price data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw dividend adjusted price data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated dividend adjusted price data in the database schema format
        """
        if not data:
            return []
        
        translated_prices = []
        for price in data:
            translated = {
                'symbol': price.get('symbol'),
                'date': price.get('date'),
                'open': safe_float(price.get('open')),
                'high': safe_float(price.get('high')),
                'low': safe_float(price.get('low')),
                'close': safe_float(price.get('close')),
                'adj_open': safe_float(price.get('adjOpen')),
                'adj_high': safe_float(price.get('adjHigh')),
                'adj_low': safe_float(price.get('adjLow')),
                'adj_close': safe_float(price.get('adjClose')),
                'volume': safe_int(price.get('volume')),
                'unadjusted_volume': safe_int(price.get('unadjustedVolume')),
                'change': safe_float(price.get('change')),
                'change_percent': safe_float(price.get('changePercent')),
                'vwap': safe_float(price.get('vwap')),
                'label': price.get('label'),
                'change_over_time': safe_float(price.get('changeOverTime')),
            }
            translated_prices.append(translated)
        
        return translated_prices

    @staticmethod
    def translate_prices(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates price data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw price data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated price data in the database schema format
        """
        if not data:
            return []
        
        translated_prices = []
        for price in data:
            translated = {
                'symbol': price.get('symbol'),
                'date': price.get('date'),
                'open': safe_float(price.get('open')),
                'high': safe_float(price.get('high')),
                'low': safe_float(price.get('low')),
                'close': safe_float(price.get('close')),
                'volume': safe_int(price.get('volume')),
                'change': safe_float(price.get('change')),
                'change_percent': safe_float(price.get('changePercent')),
                'vwap': safe_float(price.get('vwap')),
            }
            translated_prices.append(translated)
        
        return translated_prices

    @staticmethod
    def translate_dividends(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates dividends data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw dividends data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated dividends data in the database schema format
        """
        if not data:
            return []
        
        translated_dividends = []
        for dividend in data:
            translated = {
                'symbol': dividend.get('symbol'),
                'date': dividend.get('date'),
                'declaration_date': dividend.get('declarationDate'),
                'adj_dividend': safe_float(dividend.get('adjDividend')),
                'dividend': safe_float(dividend.get('dividend')),
                'yield': safe_float(dividend.get('yield')),
                'frequency': dividend.get('frequency'),
            }
            translated_dividends.append(translated)
        
        return translated_dividends

    @staticmethod
    def translate_splits(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates splits data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw splits data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated splits data in the database schema format
        """
        if not data:
            return []
        
        translated_splits = []
        for split in data:
            translated = {
                'symbol': split.get('symbol'),
                'date': split.get('date'),
                'numerator': int(split.get('numerator')) if split.get('numerator') is not None else None,
                'denominator': int(split.get('denominator')) if split.get('denominator') is not None else None,
            }
            translated_splits.append(translated)
        
        return translated_splits 