"""
Write a Python function that takes a list as an argument and returns a new list containing only the unique elements from the original list, in the same order.
Sample input: [1, 2, 3, 3, 3, 3, 4, 5, 1, 3, 5, 5, 5]
Expected output: [1, 2, 3, 4, 5]
"""


def unique_elements(old_list):
    new_list = []

    for num in old_list:

        if num not in new_list:
            new_list.append(num)

    return new_list

print(unique_elements([1, 2, 3, 3, 3, 3, 4, 5, 1, 3, 5, 5, 5]))