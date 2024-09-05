from langchain_openai import OpenAI
llm = OpenAI(model_name="gpt-3.5-turbo-instruct")
print(llm.invoke("ITエンジニアについて30文字以内で教えて。"))