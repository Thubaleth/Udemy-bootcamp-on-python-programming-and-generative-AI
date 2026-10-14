"""
Analyze chatbot conversations.

Example file:
chat.txt

User: hello
Bot: Hi there!
User: how are you
Bot: I'm fine!

Requirements:
- Count user messages
- Count bot messages
- Find most common user words
- Display conversation statistics
"""


with open("chat.txt") as chat_file:
    content = chat_file.read().splitlines()

   
    count_user = 0
    count_bot = 0 
    user_words = []
    word_count = {}

    for line in content:
        parts = line.split(": ", 1)
        sender = parts[0]
        if 'User' in sender:
            count_user += 1
        elif 'Bot' in sender:
            count_bot += 1
    
   

    for word in user_words:

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


    # Find most common word
    most_common_word = None
    max_count = 0

    for word, count in word_count.items():
        if count > max_count:
            max_count = count
            most_common_word = word


    # Output
    print("User messages:", count_user)
    print("Bot messages:", count_bot)
    print("Most common user word:", most_common_word, max_count)
        


    