from langchain_community.document_loaders import GitLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator

from langchain_openai import OpenAI
from dotenv import load_dotenv
import os
# 環境変数の読み込み
load_dotenv()

llm = OpenAI(temperature=0)

clone_url = "https://github.com/msdsm/partial-super-resolution"
branch = "main"
repo_path = "./temp/"
filter_ext = ".py"

if os.path.exists(repo_path):
    clone_url = None

loader = GitLoader(
    clone_url=clone_url,
    branch=branch,
    repo_path=repo_path,
    file_filter=lambda file_path: file_path.endswith(filter_ext),
)

index = VectorstoreIndexCreator(
    vectorstore_cls=Chroma,
    embedding=OpenAIEmbeddings(disallowed_special=()),
).from_loaders([loader])

query = "このリポジトリは何をしていますか？"
answer = index.query(query, llm=llm)
print(answer)