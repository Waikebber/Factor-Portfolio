from typing import List, Dict, Optional, Union
from .BaseGetter import BaseGetter

class GetMacroData(BaseGetter):
    def get_economic_indicators(
        self,
        names: Union[str, List[str]],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        if isinstance(names, str):
            names = [names]
        selected_columns = ", ".join(columns) if columns else "*"
        name_placeholders = ", ".join(["?"] * len(names))
        params = names[:]
        where_clause = f"name IN ({name_placeholders})"
        if start_date:
            where_clause += " AND date >= ?"
            params.append(start_date)
        if end_date:
            where_clause += " AND date <= ?"
            params.append(end_date)
        query = f"SELECT {selected_columns} FROM economic_indicators WHERE {where_clause}"
        return self._fetch_all(query, tuple(params))

    def get_industry_pe(self, start_date=None, end_date=None, columns=None) -> List[Dict]:
        return self._query_with_dates("industry_pe", start_date, end_date, columns)

    def get_industry_performance(self, start_date=None, end_date=None, columns=None) -> List[Dict]:
        return self._query_with_dates("industry_performance", start_date, end_date, columns)

    def get_sector_pe(self, start_date=None, end_date=None, columns=None) -> List[Dict]:
        return self._query_with_dates("sector_pe", start_date, end_date, columns)

    def get_sector_performance(self, start_date=None, end_date=None, columns=None) -> List[Dict]:
        return self._query_with_dates("sector_performance", start_date, end_date, columns)

    def get_treasury_rates(self, start_date=None, end_date=None, columns=None) -> List[Dict]:
        return self._query_with_dates("treasury_rates", start_date, end_date, columns)

    def get_mergers_acquisitions(
        self,
        symbols: Optional[List[str]] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        columns: Optional[List[str]] = None
    ) -> List[Dict]:
        selected_columns = ", ".join(columns) if columns else "*"
        conditions = []
        params = []

        if symbols:
            conditions.append("symbol IN ({})".format(", ".join(["?"] * len(symbols))))
            params.extend(symbols)
        if start_date:
            conditions.append("transaction_date >= ?")
            params.append(start_date)
        if end_date:
            conditions.append("transaction_date <= ?")
            params.append(end_date)

        where_clause = "WHERE " + " AND ".join(conditions) if conditions else ""
        query = f"SELECT {selected_columns} FROM mergers_acquisitions {where_clause}"
        return self._fetch_all(query, tuple(params))

    def _query_with_dates(
        self, table_name: str, start_date: Optional[str], end_date: Optional[str], columns: Optional[List[str]]
    ) -> List[Dict]:
        selected_columns = ", ".join(columns) if columns else "*"
        query = f"SELECT {selected_columns} FROM {table_name}"
        conditions = []
        params = []
        if start_date:
            conditions.append("date >= ?")
            params.append(start_date)
        if end_date:
            conditions.append("date <= ?")
            params.append(end_date)
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        return self._fetch_all(query, tuple(params))
