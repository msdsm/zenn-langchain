from langchain.callbacks import StdOutCallbackHandler
from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(model_name="gpt-3.5-turbo-instruct")
prompt = PromptTemplate.from_template("1 + {number} = ")

# chain = LLMChain(llm=llm, prompt=prompt)
chain = prompt | llm
print(chain.invoke(2))

handler = StdOutCallbackHandler()
chain = LLMChain(llm=llm, prompt=prompt, callbacks=[handler])
print(chain.run(number=2))