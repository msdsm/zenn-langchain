# Document Loadersの使用例
# 質問文と関連度の高いPDFのページのindexとその内容を表示

# from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader

# from langchain.vectorstores import Chroma
from langchain_community.vectorstores import Chroma

# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings

# 読み込み
loader = PyPDFLoader("https://blog.freelance-jp.org/wp-content/uploads/2023/03/FreelanceSurvey2023.pdf")
pages = loader.load_and_split()
print(pages[0])

chroma_index = Chroma.from_documents(pages, OpenAIEmbeddings())
docs = chroma_index.similarity_search("「フリーランスのリモートワークの実態について教えて。」", k=2)
for doc in docs:
    print(str(doc.metadata["page"]) + ":", doc.page_content)