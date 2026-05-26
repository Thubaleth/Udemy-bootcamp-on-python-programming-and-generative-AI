"""
Classify news headlines from a file.

Example file:
headlines.txt

Breaking market crash shocks investors
Local sports team wins championship
Secret government project leaked

Requirements:
- Read headlines
- Detect suspicious keywords
- Calculate fake-news score
- Print suspicious headlines
"""

with open("headline.txt") as headlines:
    content = headlines.readlines()
    key_words = ["shocks","investors","crash"]
    score = 0
    fake_news = 0
    for line in content:
        word = line.split()
        for keyword in key_words:
         if keyword in word:
            
            score += 1
            fake_news+=1
    if fake_news > 0:
       print("fake news detected")
    if score > 2:
        
        print("suspicious headlines")

    
   
        

    

        
    