import joblib
from .BaseFactor import BaseFactor

class ValueFactor(BaseFactor):
    def __init__(self, fetcher, config):
        super().__init__(fetcher, config)
        self.model = None
        if config.get("mode") == "ml":
            self.model = joblib.load(config["model_path"])

    def compute(self, data: dict) -> float:
        mode = self.config.get("mode", "rule")
        if mode == "rule":
            return self._compute_rule(data)
        elif mode == "statistical":
            return self._compute_statistical(data)
        elif mode == "ml":
            return self._compute_ml(data)
        else:
            raise ValueError(f"Unsupported mode: {mode}")

    def _compute_rule(self, data: dict) -> float:
        pe = data.get("peRatio")
        if pe is None or pe <= 0:
            return 0.0
        return 1.0 / pe

    def _compute_statistical(self, data: dict) -> float:
        value = data.get("peRatio")
        if value is None:
            return 0.0

        mean = self.config.get("mean", 0)
        std = self.config.get("std", 1)
        if std == 0:
            return 0.0

        return (value - mean) / std

    def _compute_ml(self, data: dict) -> float:
        if not self.model:
            raise RuntimeError("ML model not loaded")

        features = [data.get(k, 0) for k in self.config.get("features", ["peRatio", "pbRatio", "dcf", "price"])]
        return float(self.model.predict([features])[0])

