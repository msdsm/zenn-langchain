from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator

from langchain_openai import OpenAI
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

llm = OpenAI(temperature=0)

# Attention is all you need
loader = PyPDFLoader("https://arxiv.org/pdf/1706.03762")

index = VectorstoreIndexCreator(
    vectorstore_cls=Chroma,
    embedding=OpenAIEmbeddings(),
).from_loaders([loader])

query = "この論文のタイトルは？"

answer = index.query(query, llm=llm)
print(answer)