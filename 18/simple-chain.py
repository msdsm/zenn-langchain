from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(model_name="gpt-3.5-turbo-instruct")
prompt = PromptTemplate(
    input_variables=["job"],
    template="{job}に一番おすすめのプログラミング言語は何？",
)
chain = prompt | llm
print(chain.invoke("データサイエンティスト"))