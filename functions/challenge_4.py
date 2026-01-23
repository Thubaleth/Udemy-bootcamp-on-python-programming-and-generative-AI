#Create a function that takes an integer as an argument and returns True if it’s a prime number, and False otherwise.

def prime_number(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True
