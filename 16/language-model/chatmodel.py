from langchain_openai import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
)

chat = ChatOpenAI(model_name="gpt-3.5-turbo")
print(
    chat.invoke([
        SystemMessage(content="日本語で回答して。"),
        HumanMessage(content="ITエンジニアについて30文字で教えて。"),
    ])
)