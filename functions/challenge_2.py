#Write a Python function to check whether a number is perfect. The function should return True if the number is perfect, and False otherwise.
#📘 Learn more about perfect numbers: Perfect Number – Britannica


def perfect_num(number):
    sum = 0
    for num in range(1,number):

        if number % num == 0:
            sum += num
    
    if sum == number:
        return True
    else:
        return False
    
print(perfect_num(490))


