""""
Write a Python script that displays the following pattern from 1  to n where n is entered by the user.

If the user enters 6 it will display:

1

22

333

4444

55555

666666
"""

number = int(input("Enter the number: "))

for x in range(1,number+1):
  
    for y  in range(1,x+1):
        print(x,end=" ")
    print()
    print()
    
    


