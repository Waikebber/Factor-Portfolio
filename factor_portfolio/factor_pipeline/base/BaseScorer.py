from abc import ABC, abstractmethod
import pandas as pd

class BaseScorer(ABC):
    """
    Abstract scorer for applying trained model to compute value scores.
    """

    def __init__(self, model):
        self.model = model

    @abstractmethod
    def score(self, df: pd.DataFrame) -> pd.Series:
        """
        Returns a pd.Series of scores (e.g., ValueScore).
        """
        pass
