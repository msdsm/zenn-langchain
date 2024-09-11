from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()

memory.save_context(
    {"input": "AIとは何？"},
    {"output": "AIとは人工知能のことです。"},
)
print(memory.load_memory_variables({}))


# ConversationBufferMemoryではConversationChainのインスタンスを作るときに設定するとそれ以降のチャットを自動保存する
from langchain_openai import OpenAI
from langchain.chains import ConversationChain
llm = OpenAI(model_name="gpt-3.5-turbo-instruct")
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=ConversationBufferMemory(),
)

conversation("AIとは何？")

conversation("詳しく教えて")