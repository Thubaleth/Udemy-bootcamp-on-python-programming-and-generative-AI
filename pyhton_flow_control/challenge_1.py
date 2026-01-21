#Write a Python script that asks the user for a number and prints a list of all its divisors for each number less than the given number.

number = int(input("Enter a number: " ))
num_list = []
for num in range(1,number):
    if number % num == 0:
        num_list.append(num)

print(num_list)


