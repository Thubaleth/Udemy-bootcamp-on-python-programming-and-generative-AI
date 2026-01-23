#Write a Python function that takes an integer n as an argument and returns its factorial.
#📘 Learn more about factorials: Factorial – Wikipedia

def factorial_num(n):
    result = 1  
    
    for num in range(1, n + 1):
        result *= num  
    
    return result

print(factorial_num(5))
