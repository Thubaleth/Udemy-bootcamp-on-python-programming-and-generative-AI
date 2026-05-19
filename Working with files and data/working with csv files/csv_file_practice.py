import csv

with open('working with csv files\model_logs.csv','r') as csvfile:
    reader = csv.reader(csvfile)#reads each row as a list
    next(reader)
    token_data = {}

for row in reader:
    key = row[0]
    value = int(row[3])

    token_data[key] = value
    
    
print(token_data) #To store each day as a key and the numbers as a value

