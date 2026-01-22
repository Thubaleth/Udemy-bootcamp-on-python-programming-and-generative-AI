"""
Write a Python script that draws the following pattern using for loops.

*

* *

* * *

* * * *

* * * * *

* * * *

* * *

* *

*
"""

for x in range(1,6):
    for y in range(x):
        print("*",end ="")
    print()
    print()

for i in range(5,0,-1):
    for z in range(i):
         print("*",end ="")
    print()
    print()

        