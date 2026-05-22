"""Classify user intent.

intents = {
    "weather": ["rain", "sunny", "temperature"],
    "music": ["song", "music", "artist"],
    "food": ["pizza", "burger", "restaurant"]
}

Requirements:
- Ask user for sentence
- Detect matching keywords
- Predict user intent
"""
intents = {
    "weather": ["rain", "sunny", "temperature"],
    "music": ["song", "music", "artist"],
    "food": ["pizza", "burger", "restaurant"]
}

def Detect_matching_words():
    sentence = input("Enter your sentence: ")
    lst_sentence = sentence.split()
    for intent,words in intents.items():
        for word in words:
            if word in lst_sentence:
                return f"{word} is a matching word"
            
    return "No matching words"

def predict_user_intent():

    sentence = input("Enter your sentence: ")
    lst_sentence = sentence.split()
    for intent,words in intents.items():
        for word in words:
            if word in lst_sentence:
                return f"user intent is {intent}"
        
    return "No user intent found"
        

   

