from typing import List, Dict, Optional, Union
from .BaseGetter import BaseGetter

class GetGrowth(BaseGetter):
    def get_balance_sheet_growth(
        self,
        tickers: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        return self._query("balance_sheet_growth", tickers, start_date, end_date, columns)

    def get_cashflow_statement_growth(
        self,
        tickers: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        return self._query("cashflow_statement_growth", tickers, start_date, end_date, columns)

    def get_financial_statement_growth(
        self,
        tickers: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        return self._query("financial_statement_growth", tickers, start_date, end_date, columns)

    def get_income_statement_growth(
        self,
        tickers: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        return self._query("income_statement_growth", tickers, start_date, end_date, columns)

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
