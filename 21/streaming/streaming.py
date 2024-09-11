# on_llm_new_token実装

from typing import Any
from uuid import UUID
from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.outputs import ChatGenerationChunk, GenerationChunk
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

class MyStreamingHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        print(f"My custom handler, token: {token}")


chat = ChatOpenAI(max_tokens=50, streaming=True, callbacks=[MyStreamingHandler()])
chat([HumanMessage(content="大規模言語モデルについて30文字以内で教えてください")])