from abc import ABC, abstractmethod
import pandas as pd

# creating this class to enforce a  pattern

class PriceSource(ABC):
    @abstractmethod
    def get_prices(self, ticker: str, start: str, end: str) -> pd.DataFrame:
        """Returns a tidy frame: date, ticker, open, high, low, close, volume."""
        ...
