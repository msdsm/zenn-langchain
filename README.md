# サクッと始めるプロンプトエンジニアリング(LangChain/ChatGPT)

## ソース
- https://zenn.dev/umi_mori/books/prompt-engineer

## 内容
- 1 : はじめに
- 2 : プロンプトエンジニアとは
- 3 : プロンプトエンジニアの必須スキル5選
- 4 : プロンプトデザイン入門
- 5 : LangChainの概要と使い方
- 6 : LangChainのインストール方法(python)
- 7 : LangChainのインストール方法(js, ts)
- 8 : LCEL(LangChain Expression Language)の概要と使い方
- 9 : LangSmithの概要と使い方(LLMOps)
- 10 : LangServeの概要と使い方(API)
- 11 : LangGraphの概要と使い方(Multi-Actor)
- 12 : OpenGPTsの概要と使い方
- 13 : LangChain Evaluations
- 14 : LangChain Hub
- 15 : OpenAI Evalsとは
- 16 : LangChain Model I/Oとは
- 17 : LangChain Retrievalとは
- 18 : LangChain Chainsとは
- 19 : LangChain Memoryとは
- 20 : LangChain Agentsとは
- 21 : LangChain Callbacksとは
- 22 : ChatGPTのウェブアプリ開発入門
- 23 : LangChainによる「YouTube動画を学習させる方法」
- 24 : LangChainによる「特定のウェブページを学習させる方法」
- 25 : LangChainによる「特定のPDFを学習させる方法」
- 26 : LangChainによる「GitHubリポジトリを学習させる方法」
- 27 : LangChainによる「演算機能を学習させる方法」
- 28 : LangChainによる「ウェブ検索機能を搭載する方法(Google API)」
- 29 : LangChainによる「ウェブ検索機能を搭載する方法(Bing API)」
- 30 : LangChainによる「ウェブ検索機能を搭載する方法(DuckDuckGo API)」
- 31 : LangChainによる「Pandasのデータフレームを操作する方法」
- 32 : LangChainによる「SQL操作をする方法」
- 33 : LangChainによる「文献参照をする方法」
- 34 : 最後に


## 構成
- 05
  - langchain-main.py : LangChain使用
  - anthropic-main.py : anthropic使用
- 10
  - server.py : LangServeを使用したServer
  - client.py : Client
- 11
  - main.py : LangGraph
- 16
  - prompt : Promptsの例
    - template
      - prompt.py
      - fewshotprompt.py
      - chatprompt.py
    - example-selector
      - main.py
  - language-model : Language Modelsの例
    - llm.py
    - chatmodel.py
  - output-parser : Output Parserの例
    - list-parser.py
    - pydantic-parser.py
    - auto-fixing-parser.py
- 17
  - document-loaders : Document Loadersの例
  - document-transformers : Document Transformersの例
  - openai-embeddings : Text Embedding Modelsの例
  - vector-store : Vector Storeの例
  - retrievers : Retrieversの例
  - indexing : Indexingの例(elastic-search-store)
- 18
  - simple-chain.py : simple chain実装
  - sequential-chain.py : sequential chain実装
  - custom-chain.py : 自作chain実装
- 19
  - chat-message-history.py : Chat Message History実装
  - simple-history.py : Simple History実装
  - buffer-memory.py : Buffer Memory実装
- 20
  - tools.py : Toolsの実装例
  - agents.py : Agentsの実装例
  - toolkits.py : ToolKitsの実装例
  - agent-executor.py : Agent Executorの実装例
- 21
  - logging
  - streaming
  - token-count

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
- LangChainのツール群に含まれる1つで各LLMエージェントのステップなどをグラフ化して状態管理を行うツール
- ステートマシンを作成して複数のエージェントが協調して動作するマルチエージェントの構築を容易にすることを目的に開発
- 以下、単純なグラフの構築例でわかりやすい
  - https://zenn.dev/pharmax/articles/8796b892eed183

### Tavily API
- TavilyはAIエージェント専用に構築された検索エンジン
- https://note.com/npaka/n/n9fe8a607c56e


### OpenGPTs
- OpenAIのGPTsと類似したものを作りだすオープンソースの取り組み
- https://github.com/langchain-ai/opengpts

### LangChain Evaluations
- LangChainの評価機能
- Embedding, LLMによって評価する
- https://github.com/langchain-ai/opengpts

### LangChain Hub
- prompt template, Chain, Agentなどが上げられている
  - https://smith.langchain.com/hub
- pathを指定することで自由にloadして使用可能

### OpenAI Evals
- OpenAI社が提供するLLMコンポーネントの評価フレームワーク
- https://github.com/openai/evals
- https://qiita.com/Akifumi_Nakamura/items/f51abb811ec367440da9

### LangChain Model I/O
- 以下のように分類できる
  - Prompts : プロンプトを管理する機能
    - Prompt templates : プロンプトをテンプレート化する機能
    - Example selectors : 大量のデータから選択する機能
  - Language models : モデルを切り替えたり組み合わせたりする機能
    - LLMs : LLMモデルの機能
    - Chat models : チャット機能
  - Output parsers : 出力のデータ形式を指定するための機能
- 以下、ソースコードをもとに解説

#### Prompts
- Prompt templateの例として以下の3種
  - PromptTemplate : 16/prompt/template/prompt.py
  - FewShotPromptTemplate : 16/prompt/template/fewshotprompt.py
  - ChatPromptTemplate : 16/chatprompt.py
- Example selectorの例は以下
  - Example selector : 16/prompt/example-selector/main.py

#### Language models
- Language modelsの例として以下実装
  - LLMs : 16/language-model/llm.py
  - Chat models : 16/language-model/chatmodel.py
#### Output parsers
- Output Parserの例として以下実装
  - List parser : 16/output-parser/list-parser.py
  - Pydantic(JSON) parser : 16/output-parser/pydantic-parser.py
  - Auto-fixing parser : 16/output-parser/auto-fixing-parser.py

### LangChain Retrieval
- 外部データを用いて回答を生成する機能
- 以下の6つの機能がある
  - Document loaders
  - Document transformers
  - Text embedding models
  - Vector stores
  - Retrievers
  - Indexing
- 以下例として実装
  - Document loaders : document-loaders.py
  - Document transformers : document-transformers.py
  - Text embedding models : openai-embeddings.py
  - Vector stores : vector-store.py
  - Retrievers : retrievers.py
  - Indexing : elastic-search-store.py(windows動かない)

#### Document loaders
- PDFやCSVなどのデータを読み込むための機能

#### Document transformers
- 読み込まれた文書やテキストデータを大規模言語モデルが扱いやすい形に変換する機能
- Document transformersで代表的なモジュールであるText splittersは文章データを分割するための機能

#### Text embedding models
- 自然言語の文章や単語を数値のベクトルに変換するモデル

#### Vector stores
- ベクトル化されたデータを管理するための機能
- 代表的なデータベースとしてchromaDB
- 今回の例(17/vecotr-store.py)では、VectorStoreIndexCreatorを使用
- https://api.python.langchain.com/en/latest/indexes/langchain.indexes.vectorstore.VectorStoreIndexWrapper.html#langchain.indexes.vectorstore.VectorStoreIndexWrapper

#### Retrievers
- ドキュメント検索をするための機能
- ChatGPT Plugin Retrievers, ElasticSearch BM25やVectorStore Retrieverなど様々なRetrieverがある

#### Indexing
- 大量のテキストデータを効率よく検索できるように整理・構造化する機能


### LangChain Chains
- 18/simple-chain.py, 18/sequential-chain.py参考
- simple chainはprompt->llmという処理を実装
- sequential chainはprompt->llm->prompt->llm
  - ある生成結果を利用して新しくプロンプトを作成するというもの
- Custom ChainはChainクラスを継承する形でオリジナルのChainを作成するもの
  - custom-chain.py動かない

### CoTプロンプティング
- Chain of Thoughtプロンプティングとは入力を与える際に思考の過程をガイドとして与えることにより、より望んだ出力が得られるようにするプロンプト作成テクニックのこと

### LangChain Memory
- ChainやAgentの内部における状態保持をする機能
- 代表的なものとして以下がある
  - Chat Message History : `19/chat-message-history.py`
  - Simple Memory : `19/simple-memory.py`
  - Buffer Memory : `19/buffer-memory.py`
#### Chat Message History
- Chatの履歴データを管理するための機能
- ユーザーが送信したチャットメッセージは`add_user_message()`メソッドで追加
- LLMが生成したメッセージは`add_ai_message()`メソッドで追加
#### Simple Memory
- Chain上で最初に設定できる共有メモリの機能
- 時間や場所などの前提情報を格納できる
#### Buffer Memory
- ChainsやAgents間で履歴データを共有するためのメモリ機能
- Buffer Memoryを使用することでチャットを実行するたびに履歴データが自動的に更新される
### LangChain Agent
- 言語モデルに渡されたツールを用いてモデル自体が次にどのようなアクションをとるかを決定、実行、観測して完了するまで繰り返す機能
- LangChain Agentsの機能は以下の4つ
  - Tools : `20/tools.py`
  - Agents : `20/agents.py`
  - Toolkits : `20/toolkits.py`
  - Agent Executor : `20/agent-executor.py`
#### Tools
- Agentというロボットが外界とやり取りをするための機能

#### Agents
- プロンプトの内容に応じてツールを使い分け自動で解法を生成するロボットの機能
- 以下の4種類がある
  - zero-shot-react-description : ツールの説明文章などからどのツールを用いるかを決めるAgent
  - react-docstore : 文書を扱うことに特化したAgent
  - self-ask-with-search : 質問に対する答えを事実に基づいて調べてくれるAgent
  - conversatioinal-react-description : 会話を扱うことに特化したAgent

#### Toolkits
- 特定のユースケースに応じてツールを初期搭載したAgentの機能

#### Agent Executor
- Agentの行動を実行するための機能

### LangChain Callbacks
- LLMのアプリケーションのロギング、モニタリング、ストリーミングなどを効率的に管理する機能
- 代表的なコールバックハンドラの各メソッドに対応しているイベントは以下



| イベント名            | 説明                                    |
|-----------------------|-----------------------------------------|
| `on_llm_start`        | LLMの動作開始時                         |
| `on_chat_model_start` | チャットモデルの動作開始時               |
| `on_llm_new_token`    | 新しいLLMトークン時（ストリーミングが有効な場合のみ） |
| `on_llm_end`          | LLMの動作終了時                         |
| `on_llm_error`        | LLMでエラーが発生した時                 |
| `on_chain_start`      | チェーンの動作開始時                    |
| `on_chain_end`        | チェーンの動作終了時                    |
| `on_chain_error`      | チェーンでエラーが発生した時            |
| `on_tool_start`       | ツールの動作開始時                     |
| `on_tool_end`         | ツールの動作終了時                     |
| `on_tool_error`       | ツールでエラーが発生した時              |
| `on_text`             | 任意のテキストが出力された時            |
| `on_agent_action`     | エージェントアクション時                |
| `on_agent_finish`     | エージェントの終了時                    |



- callbacksには以下の3つの機能がある
  - Logging
  - Streaming
  - Token Count
#### Logging
- プログラムの実行中に発生するイベントやデータを記録する機能
- 各イベントをコンソールに出力する`StdOutCallbackHandler`や各イベントをファイルに保存する`FileCallbackHandler`がある
- `21/logging/stdoutcallbackhandler.py`, `21/logging/filecallbackhandler.py`

#### Streaming
- リアルタイムでデータを送受信する機能
- `on_llm_new_token`は新しいトークンが生成されるたびに呼び出され生成されたデータをリアルタイムで受け取れる

#### Token Count
- トークンカウントは言語モデルで消費されるトークン数を計測する機能
- トークンとはテキストを最小単位に分割したもの
