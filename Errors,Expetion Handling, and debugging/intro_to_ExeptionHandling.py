try:
    a = int(input("Enter a num"))
    b = int(input("Enter a num"))
    c = a /b
    print(c)
except:#runs if there is error on try
    print("An exeption has occured")
else: #runs with try
    print("No errors")
finally:  #always runs
    print("Goodbye")
    print("----------------------------------------------------------------------------------------------")



    a = 2
b = '0'
try:
    c = a / b
except Exception as e: #this catches the error
    print('This is the except block of code')
else:
    print('This is the else block of code')
finally:
    print('This is the finally block of code')
print('Continue script execution...')