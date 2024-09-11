# Toolkitsの例としてcreate_python_agent
# create_python_agentはpythonコードを実行することに特化したagent
# 動かない

from langchain_openai import OpenAI
from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool

llm = OpenAI(model_name="gpt-3.5-turbo-instruct")
agent_executor = create_python_agent(
    llm=llm,
    tool=PythonREPLTool(),
    verbose=True,
)
agent_executor.run("5つ目の素数は何？")