# サクッと始めるプロンプトエンジニアリング(LangChain/ChatGPT)

## ソース
- https://zenn.dev/umi_mori/books/prompt-engineer

## 内容
1 : はじめに
2 : プロンプトエンジニアとは
3 : プロンプトエンジニアの必須スキル5選
4 : プロンプトデザイン入門
5 : LangChainの概要と使い方
6 : LangChainのインストール方法(python)
7 : LangChainのインストール方法(js, ts)
8 : LCEL(LangChain Expression Language)の概要と使い方
9 : LangSmithの概要と使い方(LLMOps)
10 : LangServeの概要と使い方(API)
11 : LangGraphの概要と使い方(Multi-Actor)
12 : OpenGPTsの概要と使い方
13 : LangChain Evaluations
14 : LangChain Hub
15 : OpenAI Evalsとは
16 : LangChain Model I/Oとは
17 : LangChain Retrievalとは
18 : LangChain Chainsとは
19 : LangChain Memoryとは
20 : LangChain Agentsとは
21 : LangChain Callbacksとは
22 : ChatGPTのウェブアプリ開発入門
23 : LangChainによる「YouTube動画を学習させる方法」
24 : LangChainによる「特定のウェブページを学習させる方法」
25 : LangChainによる「特定のPDFを学習させる方法」
26 : LangChainによる「GitHubリポジトリを学習させる方法」
27 : LangChainによる「演算機能を学習させる方法」
28 : LangChainによる「ウェブ検索機能を搭載する方法(Google API)」
29 : LangChainによる「ウェブ検索機能を搭載する方法(Bing API)」
30 : LangChainによる「ウェブ検索機能を搭載する方法(DuckDuckGo API)」
31 : LangChainによる「Pandasのデータフレームを操作する方法」
32 : LangChainによる「SQL操作をする方法」
33 : LangChainによる「文献参照をする方法」
34 : 最後に


## 構成
- 05
  - langchain-main.py : LangChain使用
  - anthropic-main.py : anthropic使用

## メモ

### Anthropic API
- AnthropicはOpenAIの元メンバーによって設立された会社で、Claudeを開発したところ
- anthropic apiはpythonコードでClaude3を使える
```python
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
)
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "こんにちは！Claude3。今日からよろしくね。私の新しい相棒さん"}
    ]
)
print(message.content)
```

### LCEL(LangChain Expression Language)
- LCELとはLangChain特有のChainsを実装するための新しい記法
- `** | **`のように`|`で繋ぐ
- これは左の出力を右の入力として右の出力を得るという意味
- 例として以下のRAGを実装したコードを考える
```python
chain = setup_and_retrieval | prompt | model | output_parser
```
- これは以下のことをやっている
  - 入力された質問に対して文書を検索してプロンプトに渡す
  - 検索結果も含めたプロンプトを作成して言語モデルに渡す
  - 言語モデルが受け取ったプロンプトをもとに出力する
  - その出力を文字列に変換する
- 参考
  - https://book.st-hakky.com/data-science/langchain-lcel/
  - https://zenn.dev/os1ma/articles/acd3472c3a6755
  - https://qiita.com/hiromitsu_iwasaki/items/7d471ba05b0ecc582489


### LangSmith
- LangChain社のLLMOpsツール
- GUIで様々な機能がある
  - 実行トレース管理機能
  - データセット管理機能
  - アノテーション機能
- 参考
  - https://tech-blog.abeja.asia/entry/langsmith-202402

### LangServe
- LCELで作成したチェーンやエージェントをサーバーにデプロイできるパッケージ
- ソースコード(10/server.py, 10/client.py)参考
  - FastAPIを使用しているので`python server.py`実行後にlocalhost:8000/docsでswaggerUI見れる
- 参考
  - https://qiita.com/isanakamishiro2/items/fe6e80ee5860837c2987
  - https://book.st-hakky.com/data-science/langchain-langserve/

### LangGraph