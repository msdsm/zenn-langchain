# ElasticSearchStoreの使用例

from langchain_openai import OpenAIEmbeddings
from langchain.indexes import SQLRecordManager, index
from langchain.schema import Document
# from langchain_community.vectorstores import ElasticsearchStore
from langchain_elasticsearch import ElasticsearchStore

# usersというコレクションを作成
collection_name = "users"

embedding = OpenAIEmbeddings()

# ElasticsearchStoreのVector Storeを初期化
vectorstore = ElasticsearchStore(
    es_url="http://localhost:9200",
    index_name="users",
    embedding=embedding,
)