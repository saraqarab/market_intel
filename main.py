# from src.langfuse_logging import LangfuseLogging
from src.yfinance_adapter import YFinanceAdapter
from src.agent import Agent
from src.price_source import PriceSource
from src.utils import Utils
from fastapi import FastAPI

app = FastAPI()


def get_price_source() -> PriceSource:
    return YFinanceAdapter()


@app.get("/")
def read_root():
    ticker = "AAPL"
    start = "2026-01-01"
    end = "2026-06-15"
    source = get_price_source()
    df = source.get_prices(ticker=ticker, start=start, end=end)
    Utils.store_data(df, f"{ticker.lower()}_{start}_to_{end}.csv")
    agent = Agent(df)
    response = agent.call_ollama("How's the market for this stock looking today?")
    return {"response": str(response)}
