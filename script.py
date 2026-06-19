from src.agent import Agent
from src.price_source import PriceSource
from src.yfinance_adapter import YFinanceAdapter
from src.utils import Utils
import sys


def get_price_source() -> PriceSource:
    return YFinanceAdapter()


def agent():
    while True:
        user_input=str(input(""))
        ticker = "AAPL"
        start = "2026-01-01"
        end = "2026-06-15"
        if user_input == "exit":
            sys.exit(0)
        source = get_price_source()
        df = source.get_prices(ticker=ticker, start=start, end=end)
        Utils.store_data(df, f"{ticker.lower()}_{start}_to_{end}.csv")
        agent = Agent(df)

        response = agent.call_ollama(user_input)
        print(response)



print(agent())