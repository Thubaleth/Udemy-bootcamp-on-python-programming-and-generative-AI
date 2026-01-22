#Write a Python program that iterates through numbers from 1 to 50 and prints:

#"Foo" for multiples of 3

#"Bar" for multiples of 5

#"FooBar" for multiples of both 3 and 5

for num in range(1,51):
    if (num % 3 == 0 and num % 5 == 0):
        print("foobar")
    elif num % 3 == 0:
        print("foo")
    elif num % 5 == 0:
        print("bar")
    
        

