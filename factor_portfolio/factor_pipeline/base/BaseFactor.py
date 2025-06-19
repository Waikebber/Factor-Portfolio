from abc import ABC, abstractmethod

class BaseFactor(ABC):
    """
    Abstract base class for a custom factor.
    Supports multiple modes: rule-based, regression, ML.
    """

    def __init__(self, config: dict):
        self.config = config
        self.mode = config.get("mode", "rule")

    def compute(self, data):
        """
        Dispatch based on mode.
        """
        if self.mode == "rule":
            return self._compute_rule(data)
        elif self.mode == "statistical":
            return self._compute_statistical(data)
        elif self.mode == "ml":
            return self._compute_ml(data)
        else:
            raise ValueError(f"Unsupported mode: {self.mode}")

    @abstractmethod
    def _compute_rule(self, data):
        pass

    @abstractmethod
    def _compute_statistical(self, data):
        pass

    @abstractmethod
    def _compute_ml(self, data):
        pass
