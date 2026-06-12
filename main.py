
from src.yfinance_adapter import YFinanceAdapter
from src.agent import Agent


if __name__ == "__main__":
    print("data requested")
    df = YFinanceAdapter().get_prices(ticker="AAPL",start= "2024-01-01", end="2024-12-31")
    Agent = Agent(df).call_ollama('what will Apple close at tomorrow?')

