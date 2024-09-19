from langchain.chains import create_citation_fuzzy_match_runnable
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0, model="gpt-4")
chain = create_citation_fuzzy_match_runnable(llm)

question = "今の日本の総理大臣は何代目？"
context = """
内閣総理大臣（ないかくそうりだいじん、英: Prime Minister）は、日本の内閣の首長たる国務大臣。
文民である国会議員が就任し、その地位及び権限は日本国憲法や内閣法などに規定されている。
現任は、第101代岸田文雄（在任: 2021年〈令和3年〉11月10日 - ）。
""" # Wikipediaより引用

result = chain.invoke({'question': question, 'context': context})
print(result)