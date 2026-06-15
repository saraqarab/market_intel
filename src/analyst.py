import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

class Analyst:
    def __init__(self, data : pd.DataFrame):
        self.data = data


