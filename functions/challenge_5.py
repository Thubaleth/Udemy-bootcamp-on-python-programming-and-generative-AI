#========================================================
#Using the function defined in the previous challenge, find and return five prime numbers greater than 1,000,000.

def prime_number(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

