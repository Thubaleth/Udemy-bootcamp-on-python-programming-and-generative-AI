#basic regex patterns :
#-/d matches any didgit(0-9)
#-/w mathces any numeric character including underscore(a-z,A-Z,0-9)
#-/s matches any whitespaces
#(dot matches any character expect a newline.



#Quantifiers:
#+matches one or more occurences
#*matches zero or more occurences#?,atches zero or one occurences 
#?matches zero or one occurences
#{n} matches exactly n occurences
#{n,m} matches between and m occurences.

import re


post = 'Exploring the future #artificial intellegence and #machine langauge! #AI #GenAI'
hashtags = re.findall(r'#\w+',post)
print(hashtags)

