#Managing HTTP Authetication : OpenAi API
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OpenAi_API_key")

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": "you are a helpful assistant"},
        {"role": "user", "content": "What do you think are the most important inventions of the 21st century?"}
    ],
    'temperature' : 0.7
}

response = requests.post(url,headers=headers,json=data)
try:
    response.raise_for_status()#checks the https status code
    reply = response.json()['choices'][0]['message']['content']
    print(f'Assistant: {reply}')
except requests.exceptions.HTTPError as http_err:
    print(f'http error occured {http_err}')
except Exception as e:#any other error such as network error
    print(f'an unexpected error occured : {e}')