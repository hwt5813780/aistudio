import os
import openai
openai.api_key = "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"
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message.content)
