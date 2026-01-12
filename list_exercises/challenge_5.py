#Write a program that prompts the user for a string containing multiple words separated by spaces and prints the words in reverse order.

"""Example:

Input: "My name is Andrei"

Output: "Andrei is name My"
"""

str = input("Enter your name : ")

str_list = str.split()

str_list.reverse()

str_reverse = ",".join(str_list).replace(",", " ")

print(str_reverse)