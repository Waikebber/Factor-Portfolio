from typing import Callable, List, Dict, Any, Optional
from datetime import datetime
from .utils import Utils

class BaseProcessor:
    def __init__(self, config):
        self.config = config

    def process_generic(
        self,
        ticker: str,
        start_date: Optional[str],
        end_date: Optional[str],
        config_key: str,
        fetch_fn: Callable[[], List[Dict[str, Any]]],
        translate_fn: Callable[[List[Dict[str, Any]]], List[Dict[str, Any]]],
        label: str
    ) -> Optional[List[Dict[str, Any]]]:
        try:
            raw = fetch_fn()
            if not raw:
                print(f"No {label} found for {ticker}")
                return None

            translated = translate_fn(raw)
            if not translated:
                print(f"Failed to translate {label} for {ticker}")
                return None

            # Resolve config section dynamically
            config_section = getattr(self.config, config_key)

            resolved_start = start_date or config_section.get('start_date') or self.config.general_start_date
            resolved_end = end_date or config_section.get('end_date') or datetime.now().strftime('%Y-%m-%d')

            if not (start_date or end_date or config_section.get('start_date') or config_section.get('end_date')):
                return translated

            filtered = Utils.filter_by_date_range(translated, resolved_start, resolved_end)
            return filtered if filtered else None

        except Exception as e:
            print(f"Final error processing {label} for {ticker}: {e}")
            return None
