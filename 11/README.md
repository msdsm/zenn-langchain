# LangGraph
## 実行結果
```
{'messages': [HumanMessage(content='東京の天気は？'), AIMessage(content='', additional_kwargs={'function_call': {'arguments': '{"query":"東京の天気"}', 'name': 'tavily_search_results_json'}}, response_metadata={'finish_reason': 'function_call', 'model_name': 'gpt-3.5-turbo-0125'}, id='run-00e67f28-7917-4467-9f5a-75e5f0e221d2-0'), FunctionMessage(content="[{'url': 'https://weather.yahoo.co.jp/weather/jp/13/4410.html', 'content': '東京（東京）の天気予報。今日・明日の天気と風と波、明日までの6時間ごとの降水確率と最高・最低気温を見られます。'}]", name='tavily_search_results_json'), AIMessage(content='東京の天気について詳細な情報は[こちら](https://weather.yahoo.co.jp/weather/jp/13/4410.html)をご覧ください。', response_metadata={'finish_reason': 'stop', 'model_name': 'gpt-3.5-turbo-0125'}, id='run-303eb174-e059-4e2f-a000-5916a6dfeb3f-0')]}
        +-----------+
        | __start__ |
        +-----------+
               *
               *
               *
          +-------+
          | agent |
          +-------+
          .        ..
        ..           ..
       .               .
+--------+         +---------+
| action |         | __end__ |
+--------+         +---------+
```