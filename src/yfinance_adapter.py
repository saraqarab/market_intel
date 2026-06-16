import pandas as pd
import yfinance as yf

from src.utils import Utils

utils = Utils


class YFinanceAdapter:
    def __init__(self):
        self._cache = {}
        # self.fall_back_response=""

    def get_prices(self, ticker: str, start: str, end: str):
        normalized_ticker = ticker.upper()
        key = (normalized_ticker, start, end)

        if key in self._cache:
            return self._cache[key].copy()

        raw = yf.download(normalized_ticker, start=start, end=end, interval="1d", auto_adjust=True)
        if raw.empty:
            empty = pd.DataFrame(columns=["date", "ticker", "open", "high", "low", "close", "volume"])
            self._cache[key] = empty
            # self.fall_back_response = "Data could not be fetched, please try again later"
            return empty.copy()
        # incase yahoo finance returns multi indexed volumes
        if isinstance(raw.columns, pd.MultiIndex):
            raw.columns = raw.columns.get_level_values(0)
        # date index into an actual column
        df = raw.reset_index().rename(columns=str.lower)
        df["ticker"] = normalized_ticker
        result = df[["date", "ticker", "open", "high", "low", "close", "volume"]]
        self._cache[key] = result
        result.to_excel(f'data/{ticker}.xlsx', index=False)
        return result.copy() # copy because df are mutable so if I do something like df['start']=0 it'll get corrupted

