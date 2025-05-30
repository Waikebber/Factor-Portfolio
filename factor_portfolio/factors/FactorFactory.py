from .factors.ValueFactor import ValueFactor
from .factors.MomentumFactor import MomentumFactor
from .factors.BaseFactor import BaseFactor

FACTOR_CLASSES = {
    "value": ValueFactor,
    "momentum": MomentumFactor,
}

class FactorFactory:
    def __init__(self, config: dict, fetchers: dict):
        self.config = config
        self.fetchers = fetchers

    def build_factors(self) -> list:
        factors = []
        for factor_name, factor_cfg in self.config.get("factors", {}).items():
            factor_cls = FACTOR_CLASSES.get(factor_name)
            if factor_cls is None:
                raise ValueError(f"No factor class found for: {factor_name}")

            fetcher = self.fetchers.get(factor_name)
            if fetcher is None:
                raise ValueError(f"No fetcher found for factor: {factor_name}")

            factor = factor_cls(fetcher, factor_cfg)
            factors.append(factor)
        return factors
    
    def get_active_factors(self) -> list[BaseFactor]:
        return [f for f in self.build_factors() if f.config.get("active", True)]

