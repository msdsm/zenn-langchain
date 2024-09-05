from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolExecutor
from langchain_openai import ChatOpenAI
from langchain_core.utils.function_calling import convert_to_openai_function
from typing import TypedDict, Annotated, Sequence
import operator
from langchain_core.messages import BaseMessage, FunctionMessage, HumanMessage
from langgraph.prebuilt import ToolInvocation
import json
import os

# 環境変数の確認
print(os.environ["OPENAI_API_KEY"])
print(os.environ["TAVILY_API_KEY"])

# モデルのセットアップ
tools = [TavilySearchResults(max_results=1)]
tool_executor = ToolExecutor(tools)

# トークンをストリーミングするためにstreaming=Trueを設定
model = ChatOpenAI(temperature=0, streaming=True)
functions = [convert_to_openai_function(t) for t in tools]
model = model.bind_functions(functions)


# エージェントの状態を定義
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]

# 続行するかどうかを決定する関数を定義
def should_continue(state):
    messages = state['messages']
    last_message = messages[-1]
    # 関数呼び出しがない場合は終了
    if "function_call" not in last_message.additional_kwargs:
        return "end"
    # 関数呼び出しがある場合は続行
    else:
        return "continue"

# モデルを呼び出す関数を定義
def call_model(state):
    messages = state['messages']
    response = model.invoke(messages)
    # 既存のリストに追加されるのでリストを返す
    return {"messages": [response]}

# ツールを実行する関数を定義
def call_tool(state):
    messages = state['messages']
    # 継続条件に基づき、最後のメッセージが関数呼び出しを含まれている
    last_message = messages[-1]
    # 関数呼び出しからToolInvocationを構築
    action = ToolInvocation(
        tool=last_message.additional_kwargs["function_call"]["name"],
        tool_input=json.loads(last_message.additional_kwargs["function_call"]["arguments"])
    )
    # tool_executorを呼び出しレスポンスを返す
    response = tool_executor.invoke(action)
    # 応答を使ってFunctionMessageを作成
    function_message = FunctionMessage(content=str(response), name=action.tool)
    # 既存のリストに追加されるのでリストを返す
    return {"messages": [function_message]}

# グラフを定義
workflow = StateGraph(AgentState)
# 循環する2つのノードを定義
workflow.add_node("agent", call_model)
workflow.add_node("action", call_tool)
# エントリーポイントとしてagentを設定
workflow.set_entry_point("agent") # 始点
# 条件付きエッジを追加
# ("agent", should_continue)の辺を追加
# should_continueのresponseに合わせたmapping(continueならactionノード、endなら終点)
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "action",
        "end": END
    }
)
# 辺追加
workflow.add_edge("action", "agent")

# コンパイル
# LangChain Runnableにコンパイルしてほかのrunnableと同じように使用できる
app = workflow.compile()


if __name__ == "__main__":
    inputs = {"messages": [HumanMessage(content="東京の天気は？")]}
    print(app.invoke(inputs))

    # グラフの可視化
    app.get_graph().print_ascii()