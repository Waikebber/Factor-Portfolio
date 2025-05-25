from typing import Dict, Any, List
from .utils import safe_float, safe_int

class AnalysisTranslator:
    @staticmethod
    def translate_analyst_estimates(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates analyst estimates data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw analyst estimates data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated analyst estimates data in the database schema format
        """
        if not data:
            return []
            
        translated_estimates = []
        for estimate in data:
            translated = {
                'symbol': estimate.get('symbol'),
                'date': estimate.get('date'),
                'revenue_low': safe_float(estimate.get('revenueLow')),
                'revenue_high': safe_float(estimate.get('revenueHigh')),
                'revenue_avg': safe_float(estimate.get('revenueAvg')),
                'ebitda_low': safe_float(estimate.get('ebitdaLow')),
                'ebitda_high': safe_float(estimate.get('ebitdaHigh')),
                'ebitda_avg': safe_float(estimate.get('ebitdaAvg')),
                'ebit_low': safe_float(estimate.get('ebitLow')),
                'ebit_high': safe_float(estimate.get('ebitHigh')),
                'ebit_avg': safe_float(estimate.get('ebitAvg')),
                'net_income_low': safe_float(estimate.get('netIncomeLow')),
                'net_income_high': safe_float(estimate.get('netIncomeHigh')),
                'net_income_avg': safe_float(estimate.get('netIncomeAvg')),
                'sga_expense_low': safe_float(estimate.get('sgaExpenseLow')),
                'sga_expense_high': safe_float(estimate.get('sgaExpenseHigh')),
                'sga_expense_avg': safe_float(estimate.get('sgaExpenseAvg')),
                'eps_low': safe_float(estimate.get('epsLow')),
                'eps_high': safe_float(estimate.get('epsHigh')),
                'eps_avg': safe_float(estimate.get('epsAvg')),
                'num_analysts_revenue': safe_int(estimate.get('numAnalystsRevenue')),
                'num_analysts_eps': safe_int(estimate.get('numAnalystsEps'))
            }
            translated_estimates.append(translated)
        
        return translated_estimates 
    
    @staticmethod
    def translate_ratings(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Translates ratings data from the API response format to the database schema.
        
        Args:
            data (List[Dict[str, Any]]): List of raw ratings data from the API response
            
        Returns:
            List[Dict[str, Any]]: List of translated ratings data in the database schema format
        """
        if not data:
            return []
        
        translated_ratings = []
        for rating in data:
            translated = {
                'symbol': rating.get('symbol'),
                'date': rating.get('date'),
                'rating': rating.get('rating'),
                'overall_score': safe_float(rating.get('overallScore')),
                'discounted_cash_flow_score': safe_float(rating.get('discountedCashFlowScore')),
                'return_on_equity_score': safe_float(rating.get('returnOnEquityScore')),
                'return_on_assets_score': safe_float(rating.get('returnOnAssetsScore')),
                'debt_to_equity_score': safe_float(rating.get('debtToEquityScore')),
                'price_to_earnings_score': safe_float(rating.get('priceToEarningsScore')),
                'price_to_book_score': safe_float(rating.get('priceToBookScore'))
            }
            translated_ratings.append(translated)
        
        return translated_ratings 