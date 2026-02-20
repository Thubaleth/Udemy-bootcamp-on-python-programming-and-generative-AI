#Making a network automation script and I need to extract the information from the devices.txt file
#You need the Ip adress#
# you the username and the password for authentication
#and you need those files witten at the end.
#read the files into a list, where each line of the file will be another list
#the header should be excluded


with open("project-file_processing/devices.txt") as f:
    content = f.read().splitlines()
    devices = []

    for line in content[1:]:
        devices.append(line.split(':'))
    print(devices)
    
    for device in devices:
        print(f'adress is {device[1]}')


    

   


