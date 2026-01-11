"""Write a Python program to remove the character at the nth index from a non-empty string.

The nth index is provided by the user."""

char_ind = int(input("Enter the index you want to be removed :"))
str = "great"

print(str.replace(str[char_ind],""))
