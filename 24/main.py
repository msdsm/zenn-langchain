from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAI
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

# llm = OpenAI(model_name="gpt-3.5-turbo-instruct")
llm = OpenAI(temperature=0)

urls = [
    "https://zenn.dev/umi_mori/articles/what-is-gpt-4",
    "https://zenn.dev/umi_mori/articles/chatgpt-api-python",
    "https://zenn.dev/umi_mori/articles/chatgpt-google-chrome-plugins",
]

loader = UnstructuredURLLoader(urls=urls)
print(loader.load())

text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 300,
    chunk_overlap = 0,
    length_function = len,
)
print("finish text splitter")
index = VectorstoreIndexCreator(
    vectorstore_cls=Chroma,
    embedding=OpenAIEmbeddings(),
    text_splitter=text_splitter,
).from_loaders([loader])
print("finish index")
query = "7番目に紹介しているChatGPT便利プラグインは？"
answer = index.query(query)
print(answer)