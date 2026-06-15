
from src.yfinance_adapter import YFinanceAdapter
from src.agent import Agent


if __name__ == "__main__":
    df = YFinanceAdapter().get_prices(ticker="AAPL",start= "2026-01-01", end="2026-06-15")
    agent = Agent(df).call_ollama('What did the stock close on January 3rd?')

