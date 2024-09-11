from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(model_name="gpt-3.5-turbo-instruct")
prompt_1 = PromptTemplate(
    input_variables=["job"],
    template="{job}に一番おすすめのプログラミング言語は何？",
)
chain_1 = prompt_1 | llm

prompt_2 = PromptTemplate(
    input_variables=["programming_languate"],
    template="{programming_language}を学ぶためにやるべきことを3ステップで100文字で教えて。",
)
chain_2 = prompt_2 | llm

chain = chain_1 | chain_2

print(chain.invoke("データサイエンティスト"))