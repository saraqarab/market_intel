# from src.langfuse_logging import LangfuseLogging
from src.yfinance_adapter import YFinanceAdapter
from src.agent import Agent
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    df = YFinanceAdapter().get_prices(ticker="AAPL", start="2026-01-01", end="2026-06-15")
    agent = Agent(df)
    response = agent.call_ollama("How's the market for this stock looking today?")
    return {"response": str(response)}
