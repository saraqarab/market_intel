from src.langfuse_logging import LangfuseLogging
from src.yfinance_adapter import YFinanceAdapter
from src.agent import Agent
from fastapi import FastAPI


# if __name__ == "__main__":

app = FastAPI()


@app.get("/")
def read_root():
    LangfuseLogging()
    df = YFinanceAdapter().get_prices(ticker="AAPL", start="2026-01-01", end="2026-06-15")
    agent = Agent(df)
    response = agent.call_ollama('What did the stock close on January 5th?')
    print(str(response))
    return {"response": str(response)}
