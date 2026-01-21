#Write a Python program that counts and displays the vowels of a given string, ignoring the letter case.

#Input str: Hello Everybody!
#Output: 5
vowels = 'aeiou'
my_str = 'Hello Everybody'
count = 0
for v in vowels:
    if v in my_str.lower():
        count += my_str.lower().count(v)

print(f'Total number of vowels: {count}')