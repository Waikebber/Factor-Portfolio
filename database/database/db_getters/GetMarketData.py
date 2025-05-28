from typing import List, Dict, Optional, Union
from .BaseGetter import BaseGetter

class GetMarketData(BaseGetter):
    def get_price_data(
        self,
        tickers: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        return self._query("price", tickers, start_date, end_date, columns)

    def get_dividend_adjusted_prices(
        self,
        tickers: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        return self._query("dividend_adjusted_price_data", tickers, start_date, end_date, columns)

    def get_dividends(
        self,
        tickers: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        return self._query("dividends", tickers, start_date, end_date, columns)

    def get_market_cap(
        self,
        tickers: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        return self._query("market_cap", tickers, start_date, end_date, columns)

    def get_share_float(
        self,
        tickers: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        return self._query("share_float", tickers, start_date, end_date, columns)

    def get_splits(
        self,
        tickers: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        return self._query("splits", tickers, start_date, end_date, columns)

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
