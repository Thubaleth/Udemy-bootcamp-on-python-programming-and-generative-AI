"""
Analyze server logs.

Example file:
logs.txt

INFO User logged in
ERROR Database failed
INFO Request successful
ERROR API timeout

Requirements:
- Read log file
- Count ERROR messages
- Display all error lines
- Save error report to errors.txt
"""


with open("logs.txt") as log_file:
    lines = []
    for line in log_file:
    
        words = line.split()
        if 'ERROR' in words:
            lines.append(words)
        
with open("errors.txt",'w') as error_file:

    for row in lines:
       error_file.write(" ".join(row) + "\n")

    
        
    

        



  