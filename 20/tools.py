# from langchain.agents import load_tools
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import Tool
# tool_names = ["python_repl"]
# tools = load_tools(tool_names)
# print(tools)
from langchain_experimental.tools import PythonREPLTool
tools = [PythonREPLTool()]
print(tools)