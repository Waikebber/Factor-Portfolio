from typing import Any, Dict, List, Optional, Tuple
import sqlite3

class BaseGetter:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def _fetch_all(self, query: str, params: Tuple = ()) -> List[Dict[str, Any]]:
        self.conn.row_factory = sqlite3.Row
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return [dict(row) for row in cursor.fetchall()]

    def _build_conditions(
        self, tickers: List[str], start_date: Optional[str], end_date: Optional[str]
    ) -> Tuple[str, List[Any]]:
        conditions = ["symbol IN ({})".format(", ".join(["?"] * len(tickers)))]
        params = tickers[:]

        if start_date:
            conditions.append("date >= ?")
            params.append(start_date)
        if end_date:
            conditions.append("date <= ?")
            params.append(end_date)

        return " AND ".join(conditions), params
