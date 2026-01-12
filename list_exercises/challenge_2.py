#Write a Python script that removes all duplicate elements from a list.

numbers = [1,2,1,3,5,1]

new_list = []

for number in numbers:
    if number not in new_list:
        new_list.append(number)

print(new_list)