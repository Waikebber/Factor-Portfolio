from typing import List, Dict, Optional, Union
from .BaseGetter import BaseGetter

class GetAnalystData(BaseGetter):
    def get_grades(
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
        query = f"SELECT {selected_columns} FROM grades WHERE {where_clause}"
        return self._fetch_all(query, tuple(params))

    def get_grades_consensus(
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
        query = f"SELECT {selected_columns} FROM grades_consensus WHERE {where_clause}"
        return self._fetch_all(query, tuple(params))

    def get_price_target_consensus(
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
        query = f"SELECT {selected_columns} FROM price_target_consensus WHERE {where_clause}"
        return self._fetch_all(query, tuple(params))

    def get_price_target_summary(
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
        query = f"SELECT {selected_columns} FROM price_target_summary WHERE {where_clause}"
        return self._fetch_all(query, tuple(params))
