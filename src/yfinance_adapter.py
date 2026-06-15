import pandas as pd
import yfinance as yf



class YFinanceAdapter:
    def __init__(self):
        self._cache = {}

    def get_prices(self, ticker: str, start: str, end: str):
        normalized_ticker = ticker.upper()
        key = (normalized_ticker, start, end)

        if key in self._cache:
            return self._cache[key].copy()

        raw = yf.download(normalized_ticker, start=start, end=end, interval="1d", auto_adjust=True)
        if raw.empty:
            empty = pd.DataFrame(columns=["date", "ticker", "open", "high", "low", "close", "volume"])
            self._cache[key] = empty
            return empty.copy()

        if isinstance(raw.columns, pd.MultiIndex):
            raw.columns = raw.columns.get_level_values(0)

        df = raw.reset_index().rename(columns=str.lower)
        df["ticker"] = normalized_ticker
        result = df[["date", "ticker", "open", "high", "low", "close", "volume"]]
        self._cache[key] = result
        result.to_excel(f'{ticker}.xlsx', index=False)
        return result.copy()
