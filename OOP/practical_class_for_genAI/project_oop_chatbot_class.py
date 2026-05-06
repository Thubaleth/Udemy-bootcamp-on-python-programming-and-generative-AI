import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OpenAi_API_key")

class ChatBot:
    def __init__(self, api_key, model='gpt-4o-mini', temperature=0.5):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature

    def ask(self, user_message):
        try:
            client = OpenAI(api_key=self.api_key)
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {'role': 'user', 'content': user_message}
                ],
                temperature=self.temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            return f'An error occurred: {e}'


bot = ChatBot(api_key=api_key, temperature=0.7)
response = bot.ask('What are some groundbreaking AI advancements?')
print(response)
