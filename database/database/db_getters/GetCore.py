from typing import List, Dict, Optional, Union
from .BaseGetter import BaseGetter

class GetCore(BaseGetter):
    def get_stocks(
        self,
        tickers: Union[str, List[str]],
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        if isinstance(tickers, str):
            tickers = [tickers]
        selected_columns = ", ".join(columns) if columns else "*"
        placeholders = ", ".join(["?"] * len(tickers))
        query = f"SELECT {selected_columns} FROM stocks WHERE symbol IN ({placeholders})"
        return self._fetch_all(query, tuple(tickers))

    def get_employee_counts(
        self,
        tickers: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        if isinstance(tickers, str):
            tickers = [tickers]
        selected_columns = ", ".join(columns) if columns else "*"
        where_clause, params = self._build_conditions(
            tickers, start_date, end_date
        )
        query = f"SELECT {selected_columns} FROM employee_count WHERE {where_clause}"
        return self._fetch_all(query, tuple(params))
