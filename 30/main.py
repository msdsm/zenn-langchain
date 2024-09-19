# ウェブ検索機能を搭載(DuckDuckGo API)

import os
from langchain.agents import initialize_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_openai import ChatOpenAI

print(os.environ["OPENAI_API_KEY"])

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

tool_names = ["ddg-search"]
tools = load_tools(tool_names, llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True,
)

# gpt-3.5が学習していない最近の話題を聞いてみる
agent.invoke("現在の日本の総理大臣は誰ですか？")