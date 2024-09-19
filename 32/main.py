from sqlalchemy import text
from sqlalchemy import create_engine
import pandas as pd

df = pd.DataFrame({
    "name": ["佐藤", "鈴木", "吉田"],
    "age": ["20", "30", "40"],
})

sql_uri = "sqlite:///sample.db"
engine = create_engine(sql_uri, echo=False)
df.to_sql("users", con=engine)

with engine.connect() as conn:
    print(conn.execute(text("SELECT * FROM users")).fetchall())

from langchain_openai import OpenAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

db = SQLDatabase.from_uri(sql_uri)
llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0)

db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)
db_chain.run("佐藤さんの年齢は？")
db_chain.run("ユーザーの平均年齢は？")
db_chain.run("さとうさんの年齢は？")