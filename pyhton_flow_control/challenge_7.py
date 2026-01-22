"""
Write a Python program that displays the multiplication table (from 1 to 10) for a number entered by the user.

Input: User enters 8

Output:

8 x 1 = 8

8 x 2 = 16

8 x 3 = 24

8 x 4 = 32

8 x 5 = 40

8 x 6 = 48

8 x 7 = 56

8 x 8 = 64

8 x 9 = 72

8 x 10 = 80
"""

number = int(input("Enter the number from 1 to 10: "))


for i in range(1,11):
    print(f'{number} x {i} = {number*i}')
    print(" ")
    
