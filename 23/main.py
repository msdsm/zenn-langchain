import os

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.document_loaders import YoutubeLoader
from langchain_openai import OpenAI

from dotenv import load_dotenv
# 環境変数の読み込み
load_dotenv()

llm = OpenAI(temperature=0)

youtube_url = "https://www.youtube.com/watch?v=7tPMqrAoFAQ" # LangChain Indexesとは？【Document Loaders / Text Splitters / Vectorstores / Retrievers】
loader = YoutubeLoader.from_youtube_url(youtube_url)

index = VectorstoreIndexCreator(
    vectorstore_cls=Chroma, # Default
    embedding=OpenAIEmbeddings(disallowed_special=()), # Default
).from_loaders([loader])

query = "LangChain Indexesって何？"
answer = index.query(query, llm=llm)
print(answer)