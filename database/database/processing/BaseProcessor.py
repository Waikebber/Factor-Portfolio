from typing import Callable, List, Dict, Any, Optional, Union, Tuple
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
        fetch_fn: Callable[[], Any],
        translate_fn: Callable[[Any], Union[List[Dict[str, Any]], Tuple[Dict[str, Any], Dict[str, Any]]]],
        label: Union[str, Dict[str, str]]
    ) -> Optional[Union[List[Dict[str, Any]], Dict[str, List[Dict[str, Any]]]]]:
        try:
            raw = self._fetch_data(fetch_fn, label, ticker)
            if raw is None:
                return None

            translated = self._translate_data(translate_fn, raw, label, ticker)
            if translated is None:
                return None
            
            config_section = getattr(self.config, config_key)
            resolved_start, resolved_end = self._resolve_date_range(start_date, end_date, config_section)

            if isinstance(translated, tuple) and isinstance(label, dict):
                return {
                    key: [self._filter_by_date(obj, resolved_start, resolved_end, config_section, start_date, end_date)]
                    for key, obj in zip(label.keys(), translated)
                    if obj is not None
                }

            return self._filter_by_date(translated, resolved_start, resolved_end, config_section, start_date, end_date)

        except Exception as e:
            print(f"Final error processing {label} for {ticker}: {e}")
            return None
    
    def _translate_data(self, translate_fn, raw_data, label, ticker):
        translated = translate_fn(raw_data)
        if not translated:
            print(f"Failed to translate {label} for {ticker}")
            return None
        return translated

    def _resolve_date_range(self, start_date, end_date, config_section):
        resolved_start = start_date or config_section.get('start_date') or self.config.general_start_date
        resolved_end = end_date or config_section.get('end_date') or datetime.now().strftime('%Y-%m-%d')
        return resolved_start, resolved_end

    def _filter_by_date(self, data, start, end, config_section, start_arg, end_arg):
        if not (start_arg or end_arg or config_section.get('start_date') or config_section.get('end_date')):
            return data
        return Utils.filter_by_date_range(data, start, end)

    def _fetch_data(self, fetch_fn, label, ticker):
        data = fetch_fn()
        if not data:
            print(f"No {label} found for {ticker}")
            return None
        return data

