import pandas as pd
from typing import Callable, List, Tuple

class FeaturePipeline:
    def __init__(self, steps: List[Tuple[str, Callable[[pd.DataFrame], pd.DataFrame]]]):
        """
        steps: list of (name, transform_function) tuples.
        Each function should accept and return a DataFrame.
        """
        self.steps = steps

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        for name, func in self.steps:
            df = func(df.copy())
        return df
