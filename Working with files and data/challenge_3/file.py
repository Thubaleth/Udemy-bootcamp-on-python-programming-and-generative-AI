#Write a Python script that removes all empty lines, including lines that contain only spaces, from a text file.

with open("challenge_3/file.py") as f:
    content = f.readlines()
 
cleaned = []

for line in content:
    if line.strip():
        cleaned.append(line)
    
with open("challenge_3/clean_file.txt","w") as f:
    f.write(''.join(cleaned))