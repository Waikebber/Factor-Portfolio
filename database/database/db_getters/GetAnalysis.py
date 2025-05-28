from typing import List, Dict, Optional, Union
from .BaseGetter import BaseGetter

class GetAnalysis(BaseGetter):
    def get_analyst_estimates(
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

        query = f"SELECT {selected_columns} FROM analyst_estimates WHERE {where_clause}"
        return self._fetch_all(query, tuple(params))

    def get_ratings(
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

        query = f"SELECT {selected_columns} FROM ratings WHERE {where_clause}"
        return self._fetch_all(query, tuple(params))
