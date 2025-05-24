from typing import Dict, Any, List

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
                'revenue_low': float(estimate.get('revenueLow')) if estimate.get('revenueLow') is not None else None,
                'revenue_high': float(estimate.get('revenueHigh')) if estimate.get('revenueHigh') is not None else None,
                'revenue_avg': float(estimate.get('revenueAvg')) if estimate.get('revenueAvg') is not None else None,
                'ebitda_low': float(estimate.get('ebitdaLow')) if estimate.get('ebitdaLow') is not None else None,
                'ebitda_high': float(estimate.get('ebitdaHigh')) if estimate.get('ebitdaHigh') is not None else None,
                'ebitda_avg': float(estimate.get('ebitdaAvg')) if estimate.get('ebitdaAvg') is not None else None,
                'ebit_low': float(estimate.get('ebitLow')) if estimate.get('ebitLow') is not None else None,
                'ebit_high': float(estimate.get('ebitHigh')) if estimate.get('ebitHigh') is not None else None,
                'ebit_avg': float(estimate.get('ebitAvg')) if estimate.get('ebitAvg') is not None else None,
                'net_income_low': float(estimate.get('netIncomeLow')) if estimate.get('netIncomeLow') is not None else None,
                'net_income_high': float(estimate.get('netIncomeHigh')) if estimate.get('netIncomeHigh') is not None else None,
                'net_income_avg': float(estimate.get('netIncomeAvg')) if estimate.get('netIncomeAvg') is not None else None,
                'sga_expense_low': float(estimate.get('sgaExpenseLow')) if estimate.get('sgaExpenseLow') is not None else None,
                'sga_expense_high': float(estimate.get('sgaExpenseHigh')) if estimate.get('sgaExpenseHigh') is not None else None,
                'sga_expense_avg': float(estimate.get('sgaExpenseAvg')) if estimate.get('sgaExpenseAvg') is not None else None,
                'eps_low': float(estimate.get('epsLow')) if estimate.get('epsLow') is not None else None,
                'eps_high': float(estimate.get('epsHigh')) if estimate.get('epsHigh') is not None else None,
                'eps_avg': float(estimate.get('epsAvg')) if estimate.get('epsAvg') is not None else None,
                'num_analysts_revenue': int(estimate.get('numAnalystsRevenue')) if estimate.get('numAnalystsRevenue') is not None else None,
                'num_analysts_eps': int(estimate.get('numAnalystsEps')) if estimate.get('numAnalystsEps') is not None else None
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
                'overall_score': float(rating.get('overallScore')) if rating.get('overallScore') is not None else None,
                'discounted_cash_flow_score': float(rating.get('discountedCashFlowScore')) if rating.get('discountedCashFlowScore') is not None else None,
                'return_on_equity_score': float(rating.get('returnOnEquityScore')) if rating.get('returnOnEquityScore') is not None else None,
                'return_on_assets_score': float(rating.get('returnOnAssetsScore')) if rating.get('returnOnAssetsScore') is not None else None,
                'debt_to_equity_score': float(rating.get('debtToEquityScore')) if rating.get('debtToEquityScore') is not None else None,
                'price_to_earnings_score': float(rating.get('priceToEarningsScore')) if rating.get('priceToEarningsScore') is not None else None,
                'price_to_book_score': float(rating.get('priceToBookScore')) if rating.get('priceToBookScore') is not None else None
            }
            translated_ratings.append(translated)
        
        return translated_ratings 