# from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
query_result = embeddings.embed_query("ITエンジニアについて30文字で教えて。")

print(query_result)
print(len(query_result)) # 次元数