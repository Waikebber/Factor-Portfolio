from abc import ABC, abstractmethod

class BaseFactor(ABC):
    def __init__(self, fetcher, config: dict):
        self.fetcher = fetcher
        self.config = config

    @property
    def name(self) -> str:
        return self.__class__.__name__.replace("Factor", "").lower()


    @abstractmethod
    def compute(self, data: dict) -> float:
        ...

    def score(self, symbol: str, date: str) -> float:
        df = self.fetcher.fetch(symbol, date)
        row = df.iloc[0].to_dict()
        return self.compute(row)
