import pandas as pd
import requests
from bs4 import BeautifulSoup

from src.utils import Utils

utils = Utils

PSX_BASE_URL = "https://dps.psx.com.pk"
REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; market_intel/1.0)",
}


class PSXAdapter:
    """Scrapes price data from the official PSX data portal (dps.psx.com.pk)."""

    def __init__(self):
        self._cache = {}
        self._market_watch_cache = None

    def get_prices(self, ticker: str, start: str, end: str):
        normalized_ticker = ticker.upper()
        key = (normalized_ticker, start, end)

        if key in self._cache:
            return self._cache[key].copy()

        response = requests.post(
            f"{PSX_BASE_URL}/historical",
            data={"symbol": normalized_ticker},
            headers=REQUEST_HEADERS,
            timeout=10,
        )
        response.raise_for_status()

        rows = self._parse_historical_table(response.text)
        if not rows:
            empty = pd.DataFrame(columns=["date", "ticker", "open", "high", "low", "close", "volume"])
            self._cache[key] = empty
            return empty.copy()

        df = pd.DataFrame(rows)
        df["date"] = pd.to_datetime(df["date"])
        df["ticker"] = normalized_ticker
        df = df[(df["date"] >= pd.to_datetime(start)) & (df["date"] <= pd.to_datetime(end))]
        result = df[["date", "ticker", "open", "high", "low", "close", "volume"]].reset_index(drop=True)

        self._cache[key] = result
        return result.copy()

    def get_market_watch(self, force_refresh: bool = False):
        if self._market_watch_cache is not None and not force_refresh:
            return self._market_watch_cache.copy()

        response = requests.get(f"{PSX_BASE_URL}/market-watch", headers=REQUEST_HEADERS, timeout=10)
        response.raise_for_status()

        rows = self._parse_market_watch_table(response.text)
        columns = [
            "symbol", "sector", "listed_in", "ldcp", "open",
            "high", "low", "current", "change", "change_percent", "volume",
        ]
        result = pd.DataFrame(rows, columns=columns) if rows else pd.DataFrame(columns=columns)

        self._market_watch_cache = result
        return result.copy()

    def filter_by_sector(self, df: pd.DataFrame, sector: str):
        return df[df["sector"].str.casefold() == sector.casefold()].reset_index(drop=True)

    def filter_by_symbol(self, df: pd.DataFrame, symbols):
        if isinstance(symbols, str):
            symbols = [symbols]
        normalized = {s.upper() for s in symbols}
        return df[df["symbol"].str.upper().isin(normalized)].reset_index(drop=True)

    @staticmethod
    def _parse_historical_table(html: str):
        soup = BeautifulSoup(html, "html.parser")
        rows = []
        for tr in soup.select("table tbody tr"):
            cells = [td.get_text(strip=True).replace(",", "") for td in tr.find_all("td")]
            if len(cells) < 6:
                continue
            date, open_, high, low, close, volume = cells[:6]
            rows.append({
                "date": date,
                "open": float(open_),
                "high": float(high),
                "low": float(low),
                "close": float(close),
                "volume": int(float(volume)),
            })
        return rows

    @staticmethod
    def _parse_market_watch_table(html: str):
        soup = BeautifulSoup(html, "html.parser")
        rows = []
        for tr in soup.select("table tbody tr"):
            cells = [td.get_text(strip=True).replace(",", "") for td in tr.find_all("td")]
            if len(cells) < 10:
                continue
            symbol, sector, listed_in, ldcp, open_, high, low, current, change, change_pct, volume = cells[:11]
            rows.append({
                "symbol": symbol,
                "sector": sector,
                "listed_in": listed_in,
                "ldcp": float(ldcp),
                "open": float(open_),
                "high": float(high),
                "low": float(low),
                "current": float(current),
                "change": float(change),
                "change_percent": float(change_pct),
                "volume": int(float(volume)),
            })
        return rows
