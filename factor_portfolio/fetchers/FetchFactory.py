from .fetchers.ValueFactorFetch import ValueFactorFetch

FETCHER_CLASSES = {
    "value": ValueFactorFetch,
}

class FetchFactory:
    def __init__(self, config: dict):
        self.config = config

    def build_fetchers(self) -> dict:
        """
        Returns a dictionary of fetcher_name -> fetcher_instance
        """
        fetchers = {}
        for fetcher_name, fetcher_cfg in self.config.get("fetchers", {}).items():
            fetcher_cls = FETCHER_CLASSES.get(fetcher_name)
            if fetcher_cls is None:
                raise ValueError(f"No fetcher class found for: {fetcher_name}")
            fetchers[fetcher_name] = fetcher_cls(fetcher_cfg)
        return fetchers
