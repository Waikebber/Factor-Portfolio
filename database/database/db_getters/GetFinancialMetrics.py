from typing import List, Dict, Optional, Union
from .BaseGetter import BaseGetter

class GetFinancialMetrics(BaseGetter):
    def get_earnings(
        self,
        tickers: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        if isinstance(tickers, str):
            tickers = [tickers]
        selected_columns = ", ".join(columns) if columns else "*"
        where_clause, params = self._build_conditions(tickers, start_date, end_date)
        query = f"SELECT {selected_columns} FROM earnings WHERE {where_clause}"
        return self._fetch_all(query, tuple(params))

    def get_financial_ratios(
        self,
        tickers: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        if isinstance(tickers, str):
            tickers = [tickers]
        selected_columns = ", ".join(columns) if columns else "*"
        where_clause, params = self._build_conditions(tickers, start_date, end_date)
        query = f"SELECT {selected_columns} FROM financial_ratios WHERE {where_clause}"
        return self._fetch_all(query, tuple(params))

    def get_key_metrics(
        self,
        tickers: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        if isinstance(tickers, str):
            tickers = [tickers]
        selected_columns = ", ".join(columns) if columns else "*"
        where_clause, params = self._build_conditions(tickers, start_date, end_date)
        query = f"SELECT {selected_columns} FROM key_metrics WHERE {where_clause}"
        return self._fetch_all(query, tuple(params))
