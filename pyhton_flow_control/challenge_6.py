"""Given a string, write a program that calculates the sum and average of all digits in the string, ignoring other characters.

Example:

Input: "Python31py50"

Output: Sum: 9, Average: 2.25
"""

str = "Python31py50"
list = ['0','1','2','3','4','5','6','7','8','9']
sum = 0
count =0
for i in str:
    if i in list:
        sum += int(i)
        count += 1
    
average = sum/count

print(f'sum: {9}, Average: {average}')


        

