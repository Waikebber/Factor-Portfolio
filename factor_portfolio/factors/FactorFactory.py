from .ValueFactor import ValueFactor
from .MomentumFactor import MomentumFactor

FACTOR_CLASSES = {
    'value': ValueFactor,
    'momentum': MomentumFactor,
}

class FactorFactory:
    def __init__(self, config):
        self.config = config

    def build_factors(self) -> list:
        pass