#You are given a text file that contains multiple duplicate MAC addresses.
#Create a Python script that generates a new file containing only unique MAC addresses, with each address on a separate line.

with open("challenge_1/macs.txt") as f:
    macs = []
    content = f.read().splitlines()
    for line in content:
        if line not in macs:
            macs.append(line)
        
with open("challenge_1/new_macs.txt","w",newline="") as f:
    for mac in macs:
     f.write(f"{mac}")