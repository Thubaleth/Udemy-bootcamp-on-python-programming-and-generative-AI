"""Create a rule-based chatbot.

responses = {
    "hello": "Hi there!",
    "how are you": "I'm fine!",
    "bye": "Goodbye!"
}

Requirements:
- Ask user for input
- Search dictionary for response
- Print matching answer
- Show default response if unknown
"""

responses = {
    "hello": "Hi there!",
    "how are you": "I'm fine!",
    "bye": "Goodbye!"
}


def chatbot_responses():

    prompt = input("Enter your prompt: ")

    if prompt in responses:
        print(f"Bot: {responses[prompt]}")
    else:
        print("cant help you")
    
chatbot_responses()
        