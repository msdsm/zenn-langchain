from langchain.prompts import PromptTemplate
# from langchain.llms import OpenAI
from langchain_openai import OpenAI

template = """
{subject}について30文字で教えて。
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["subject"]
)

prompt_text = prompt.format(subject="ITエンジニア")
print(prompt_text) # 変数に代入できていることを確認


# ここから実際にLLM使用(PrompteTemplateとは特に関係ない)
llm = OpenAI(model_name="gpt-3.5-turbo-instruct")
# print(llm(prompt_text))
print(llm.invoke(prompt_text))