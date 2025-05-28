from typing import List, Dict, Optional, Union
from .BaseGetter import BaseGetter

class GetValuation(BaseGetter):
    def get_discounted_cash_flow(
        self,
        tickers: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        return self._query("discounted_cash_flow", tickers, start_date, end_date, columns)

    def get_levered_discounted_cash_flow(
        self,
        tickers: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        return self._query("levered_discounted_cash_flow", tickers, start_date, end_date, columns)

    def get_enterprise_values(
        self,
        tickers: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        return self._query("enterprise_values", tickers, start_date, end_date, columns)

    def get_owner_earnings(
        self,
        tickers: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        return self._query("owner_earnings", tickers, start_date, end_date, columns)

    def _query(
        self,
        table_name: str,
        tickers: Union[str, List[str]],
        start_date: Optional[str],
        end_date: Optional[str],
        columns: Optional[List[str]]
    ) -> List[Dict]:
        if isinstance(tickers, str):
            tickers = [tickers]
        selected_columns = ", ".join(columns) if columns else "*"
        where_clause, params = self._build_conditions(tickers, start_date, end_date)
        query = f"SELECT {selected_columns} FROM {table_name} WHERE {where_clause}"
        return self._fetch_all(query, tuple(params))
