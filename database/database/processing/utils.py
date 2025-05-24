from datetime import datetime
from typing import List, Dict, Any
from dataclasses import dataclass

@dataclass
class Utils:
    
    @staticmethod
    def filter_by_date_range(
        records: List[Dict[str, Any]],
        start: str,
        end: str
    ) -> List[Dict[str, Any]]:
        """Filter records by date range"""
        start_date = datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.strptime(end, '%Y-%m-%d')
        return [r for r in records if start_date <= datetime.strptime(r['date'], '%Y-%m-%d') <= end_date] 