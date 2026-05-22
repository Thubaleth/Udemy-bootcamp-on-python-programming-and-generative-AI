"""Detect suspicious keywords.

keywords = {
    "shocking": 2,
    "secret": 3,
    "breaking": 2
}

Requirements:
- Ask user for news headline
- Count suspicious words
- Calculate fake-news score
- Print warning if score is high
"""

def fake_news_keyword_detector():
    news = input("write the headlines: ")
    keywords = {}
    lst_keywords = ["shocking","secret","breaking"]
    lst_news = news.split()

    for word in lst_news:
        if word in lst_keywords:
            if word in keywords:
             keywords[word] += 1
            else:
             keywords[word] = 1
            
    
        
    return keywords

def fake_news_score(keywords):
   high_score = 5
   lst =[]
   for value in keywords.values():
      lst.append(value)

   total = sum(lst)
   if total > high_score:
      return "The fake news score is to high"
   else:
      return keywords
      
 
      
       
   
       
print(fake_news_score(fake_news_keyword_detector()))
   

  
    



    
    

