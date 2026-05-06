"""
Create a Python function called tail that reads the last n lines of a text file.
The function should accept two arguments: the file name and the number of lines to read (n).
This mimics the behavior of the Linux tail command.
Example:

tail('sample_file.txt', 5)

Returns the last 5 lines of sample_file.txt.
"""

def tail(file, n):
    with open(file, 'r') as f:
        # reading the file in a list
        content = f.read().splitlines()
        # getting the last n elements of the list
        last = content[len(content)-n:]
        # print(last)
        # concateneting the list back into a string
        my_str = '\n'.join(last)
        return my_str


t = tail('sample_file.txt', 3)
print(t)
    
    