import openai
import requests
import time
import json
openai.api_key = "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"
#  设置API请求的URL和参数

url = "https://api.openai.com/v1/chat/completions"
url2 = "https://api.openai.com/v1/images/generations"

headers = {"authority": "api.openai.com",
           "Content-Type": "application/json",
           "Authorization": "Bearer {}".format(openai.api_key)
           }

proxies = {
    "http": "http://127.0.0.1:7890",
    "https": "http://127.0.0.1:7890",
}

data = {"model": "gpt-3.5-turbo",
                    "temperature": 1,
                    "stream": True,
                    "messages": [
                        {"role": "system",
                         "content": "你是一个编写团建活动报告的机器人，我会告诉你我团建的主题和其他提示信息，\
                         你需要帮我完成markdown格式的团建活动报告的编写，要求格式美观，内容丰富，积极向上 \
                         内容要包括活动日期，参加人员，过程，活动的心得体会等等"},
                        {"role": "user", "content": "团建主题是共创美好团队生活，由智能技术产品线所有成员一起去湖山游玩"}
                    ]}
start_time = time.time()
response_time = time.time() - start_time
# create variables to collect the stream of chunks
collected_chunks = []
collected_messages = []
response = requests.post(url, headers=headers, json=data, proxies=proxies, stream=True)
for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
    chunk_time = time.time() - start_time  # calculate the time delay of the chunk
    json_data = chunk.replace('data: ', '')
    print(json_data)
    chunk_data = json.loads(json_data)
    collected_chunks.append(chunk_data)  # save the event response
    print(chunk_data)
    chunk_message = chunk_data['choices'][0]['delta']  # extract the message
    collected_messages.append(chunk_message)  # save the message
    print(f"Message received {chunk_time:.2f} seconds after request: {chunk_message}")  # print the delay and text