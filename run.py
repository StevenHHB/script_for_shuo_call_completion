import json
import requests
import os

API_KEY = os.environ.get('API_KEY')


# Endpoint URL for the OpenAI GPT-4 API
# This URL might change, check OpenAI's official docs.
endpoint = 'https://api.openai.com/v1/chat/completions'

# Headers
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
}


# Data payload
data = {
    "model": "gpt-4",
    "messages": [
        {"role": "system", "content": "你是一个中国大学生，需要根据以下的开头想象一个中国大学生可能会聊的具体话题，并且根据开头完善5个具体的可能性"},
        {"role": "user", "content": "我想"}
    ]
}

response = requests.post(endpoint, headers=headers, data=json.dumps(data))

# Extracting the response
response_json = response.json()
print(response_json)
# output = response_json['choices'][0]['text'].strip()

# print(f"Assistant's Response: {output}")
