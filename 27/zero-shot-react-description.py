from langchain_openai import OpenAI
# from langchain.agents import load_tools
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from dotenv import load_dotenv
# 環境変数の読み込み
load_dotenv()

llm = OpenAI(model_name="gpt-3.5-turbo-instruct")
tool_names = ["llm-math"]
tools = load_tools(tool_names, llm=llm)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

agent.run("""
5の3乗は？       
""")