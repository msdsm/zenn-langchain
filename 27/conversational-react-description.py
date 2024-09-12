from langchain_openai import OpenAI
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory

from dotenv import load_dotenv
# 環境変数の読み込み
load_dotenv()

llm = OpenAI(model_name="gpt-3.5-turbo-instruct")
tool_names = ["llm-math"]
tools = load_tools(tool_names, llm=llm)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
)

agent.run("""
5の3乗は？
""")

agent.run("""
その答えに対してπを掛け算するといくつ？
""")