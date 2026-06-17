from abc import ABC, abstractmethod

import pandas as pd


class PriceSource(ABC):
    @abstractmethod
    def get_prices(self, ticker: str, start: str, end: str) -> pd.DataFrame:
        """Return a tidy frame: date, ticker, open, high, low, close, volume."""
        ...
