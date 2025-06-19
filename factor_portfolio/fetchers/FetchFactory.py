from .fetchers.ValueFactorFetch import ValueFactorFetch
from .fetchers.SP500TickersFetcher import SP500TickersFetcher

FETCHER_CLASSES = {
    "value": ValueFactorFetch,
    "sp500": SP500TickersFetcher,
}

class FetchFactory:
    def __init__(self, config: dict):
        self.config = config

    def build_fetchers(self) -> dict:
        """
        Returns a dictionary of fetcher_name -> fetcher_instance
        """
        fetchers = {}
        config_fetchers = self.config.get("fetchers", {})
        
        # If no specific fetchers are requested in config, create all available ones
        if not config_fetchers:
            for fetcher_name, fetcher_cls in FETCHER_CLASSES.items():
                fetchers[fetcher_name] = fetcher_cls({})
        else:
            # Create only the fetchers specified in config
            for fetcher_name, fetcher_cfg in config_fetchers.items():
                fetcher_cls = FETCHER_CLASSES.get(fetcher_name)
                if fetcher_cls is None:
                    raise ValueError(f"No fetcher class found for: {fetcher_name}")
                fetchers[fetcher_name] = fetcher_cls(fetcher_cfg)
        
        return fetchers
