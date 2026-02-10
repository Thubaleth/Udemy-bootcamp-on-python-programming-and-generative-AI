"""
Challenge #2

Write a Python script that counts and displays the occurrences of each character in a list.
Example:
Input: list('mamma mia mm')
Output:

m ---> 6

a ---> 3

---> 2

i ---> 1
"""
chars = list('mamma mia mm')
count = {}
for ch in chars:

    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1


for key,value in count.items():
    print(f'{key} ----> {value}')
        

