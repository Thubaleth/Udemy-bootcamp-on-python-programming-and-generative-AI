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