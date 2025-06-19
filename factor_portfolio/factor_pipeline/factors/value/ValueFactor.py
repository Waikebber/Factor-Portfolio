import pandas as pd
from factor_pipeline.base.BaseFactor import BaseFactor
import joblib

class ValueFactor(BaseFactor):
    """
    Computes value factor scores using different modes (rule, statistical, ml).
    Requires z-scored input data.
    """

    def __init__(self, config: dict):
        super().__init__(config)
        self.model_path = config.get("model_path")
        self.features = config.get("features", [])

        if self.mode == "ml" and self.model_path:
            self.model = joblib.load(self.model_path)

    def _compute_rule(self, data: pd.DataFrame) -> pd.Series:
        # Example rule: average of inverse P/E and inverse P/B
        z_pe = data["z_inverse_pe"]
        z_pb = data["z_inverse_pb"]
        z_dcf = data.get("z_dcf_discount", 0)
        return (z_pe + z_pb + z_dcf) / 3

    def _compute_statistical(self, data: pd.DataFrame) -> pd.Series:
        # Example: static weights from config
        weights = self.config.get("weights", {})
        score = sum(data[feat] * weights.get(feat, 1) for feat in self.features)
        return score

    def _compute_ml(self, data: pd.DataFrame) -> pd.Series:
        if self.model is None:
            raise RuntimeError("ML model not loaded.")
        return pd.Series(self.model.predict(data[self.features]), index=data.index)
