import csv

with open('model_logs.csv','r') as csvfile:
    reader = csv.reader(csvfile)#reads each row as a list
    next(reader)
    token_data = {}

    for row in reader:
      key = row[0]
      value = int(row[3])

      token_data[key] = value #To store each day as a key and the numbers as a value
    
    peak_day = max(token_data, key = token_data.get) 
    
    print(f'Model usage:{peak_day}, Token Generated: {token_data[peak_day]}' ) #Store the max

