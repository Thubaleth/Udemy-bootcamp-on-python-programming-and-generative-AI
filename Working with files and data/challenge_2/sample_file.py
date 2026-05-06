#Create a Python script that reads a text file into a list, then converts the list into a single string containing the entire file content.


with open("challenge_2/sample_file.txt") as f:
    content = f.read().splitlines()
    for line in content:
        my_str = "\n".join(line)
        print(my_str)
