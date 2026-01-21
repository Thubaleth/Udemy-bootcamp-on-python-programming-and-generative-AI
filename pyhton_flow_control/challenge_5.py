"""Write a Python program that prompts the user for multiple float numbers and calculates:

The sum

The product

The average

Enter 0 to finish."""
total_sum = 0
product = 1
count = 0

while True:
    number = float(input("Enter a number (0 to finish): "))

    if number == 0:
        break

    total_sum += number
    product *= number
    count += 1

if count > 0:
    average = total_sum / count
else:
    average = 0
print(f"The sum is {total_sum}")
print(f"The product is {product}")
print(f"The average is {average}")

