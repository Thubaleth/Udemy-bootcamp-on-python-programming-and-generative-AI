"""Write a Python script that replaces all occurrences of the first character in a string with '$', except for the first occurrence itself.

Example:

Input: 'mama'

Output: 'ma$a'"""

my_str = input('Enter a string:')
char = my_str[0]
new_str = my_str[1:].replace(char, '$')
new_str = char + new_str
print(new_str)
