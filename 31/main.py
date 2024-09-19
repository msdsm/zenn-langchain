import pandas as pd

df = pd.DataFrame({
    "name": ["佐藤", "鈴木", "吉田"],
    "age": ["20", "30", "40"],
})
print(df.head())

from langchain_openai import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent

llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0)

agent = create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True)

agent.run("佐藤さんの年齢は？")
agent.run("ユーザーの平均年齢は？")