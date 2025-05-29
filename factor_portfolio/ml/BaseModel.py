from abc import ABC, abstractmethod
import pandas as pd

class BaseModel(ABC):
    @abstractmethod
    def fit(self, X: pd.DataFrame, y: pd.Series):
        pass

    @abstractmethod
    def predict(self, X: pd.DataFrame) -> pd.Series:
        pass

    @abstractmethod
    def save(self, path: str):
        pass

    @abstractmethod
    def load(self, path: str):
        pass

    @abstractmethod
    def evaluate(self, X: pd.DataFrame, y: pd.Series, metric: str = "r2") -> float:
        pass

