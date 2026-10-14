"""
Detect spam emails from a file.

spam_words = ["win", "free", "urgent", "money"]

Requirements:
- Read emails from emails.txt
- Count spam keywords
- Score each email
- Save spam emails to spam.txt
"""

spam_words = ["win", "free", "urgent", "money"]

with open("email.txt") as email_f:
    content = email_f.readlines()
    count_spam = 0
    count_words = {}
    for line in content:
        words =  line.split()
        for spam_word in spam_words:
        
         if spam_word not in count_words:
            count_words[spam_word] = 0

    
         if spam_word in words:
            count_words[spam_word] += 1
            
    print(count_words)
            

        
 