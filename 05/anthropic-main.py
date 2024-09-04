import anthropic
import os

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "こんにちは！Claude3。今日からよろしくね。私の新しい相棒さん"}
    ]
)
print(message.content)