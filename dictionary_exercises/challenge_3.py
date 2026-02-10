"""
Given a list of words, write a Python script that creates a dictionary where each word is a key, and its length is the value.

Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']

Expected Result: {'Python': 6, 'Java': 4, 'C++': 3, 'Golang': 6, 'Solidity': 8, 'Bash': 4}
"""

words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
dict = {}
for word in words:
  dict[word] = len(word)

print(dict)

