# openai_callback

# from langchain.callbacks import get_openai_callback
from langchain_community.callbacks.manager import get_openai_callback
from langchain_openai import OpenAI

llm = OpenAI()
with get_openai_callback() as cb:
    result = llm.invoke("大規模言語モデルについて30文字以内で教えてください。")
    print(result)
    print(cb)