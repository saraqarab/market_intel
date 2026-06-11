
#
# api_key = os.getenv("SBP_API_KEY")
# res = requests.get("https://easydata.sbp.org.pk/api/v1/series/TS_GP_BOP_WR_M.WR0010/data?api_key="+
#                            f"{api_key}" ,verify = False)
# print(res.text)
from src.price_source import PriceSource
from src.yfinance_adapter import YFinanceAdapter
from pandas import DataFrame
from pathlib import Path
from src.agent import Agent

def data(source: PriceSource, ticker: str) -> DataFrame:
    df = source.get_prices(ticker, "2024-01-01", "2024-12-31")
    return df

# if __name__ == "__main__":
#     print("data requested")
#     source = YFinanceAdapter()
#     df = data(source, "AAPL")
#     data_dir = Path("data")
#     data_dir.mkdir(parents=True, exist_ok=True)
#     output_file = data_dir / "aapl_2024.csv"
#     df.to_csv(output_file, index=False)
#     print(df)

model = Agent('ollama')
# model = Agent('ollama').call_ollama(role="user", content='what is a quark in 5 sentences?')
model.check_ollama_installation()