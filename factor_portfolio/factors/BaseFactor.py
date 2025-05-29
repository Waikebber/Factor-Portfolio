from abc import ABC, abstractmethod

class BaseFactor(ABC):
    def __init__(self, getter, config):
        self.getter = getter
        self.config = config

    @abstractmethod
    def compute(self, data: dict) -> float:
        """Compute normalized score for a given symbol"""
        ...
