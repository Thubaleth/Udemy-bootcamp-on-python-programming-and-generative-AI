"""Write a Python script that extracts the first and last two characters from a user-entered string.

Example:

Input: 'Hello!'

Output: 'Heo!'"""

str = input("Enter a word: ")

print(str[:2] + str[-2:])
