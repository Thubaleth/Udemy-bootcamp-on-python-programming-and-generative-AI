

"""
Detect spam emails.

spam_words = {
    "win": 3,
    "free": 2,
    "urgent": 2,
    "money": 3
}

Requirements:
- Ask user for email text
- Count spam keywords
- Calculate spam score
- Print "Spam" if score is high
"""

def detect_spam_emails():
    
    spam_keywords = {
        "win": 3,
        "free": 2,
        "urgent": 2,
        "money": 3
    }

    email = input("Enter the email text: ").lower()
    lst_email = email.split()

    total_score = 0

    for word in lst_email:
        if word in spam_keywords:
            total_score += spam_keywords[word]

    return total_score


def calculate_spam_score(score):

    high_score = 6

    if score >= high_score:
        return "Spam"
    else:
        return "No Spam"


score = detect_spam_emails()

print("Spam Score:", score)
print(calculate_spam_score(score))



   

   