from .BaseFactor import BaseFactor

class ValueFactor(BaseFactor):
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
        ...

    def _compute_statistical(self, data: dict) -> float:
        # Normalize each input using Z-score or percentile
        ...

    def _compute_ml(self, data: dict) -> float:
        import joblib
        model_path = self.config.get("model_path")
        model = joblib.load(model_path)

        features = [data.get("peRatio", None), data.get("pbRatio", None), data.get("dcf", None), data.get("price", None)]
        features = [x if x is not None else 0 for x in features]  # crude fallback
        return float(model.predict([features])[0])
