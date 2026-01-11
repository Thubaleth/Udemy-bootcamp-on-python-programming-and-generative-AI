#Write a Python script to check if a string is a palindrome.

palindrome = input("Enter a word: ")

if palindrome == palindrome[::-1]:
  print("The word is a palindrome")
else:
  print("word is NOT a palindrome")