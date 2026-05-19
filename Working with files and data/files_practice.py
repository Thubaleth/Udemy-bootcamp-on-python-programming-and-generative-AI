with open('') as f:
    content = f.read.splitlines()
    print(content) #output is a list off lines

#2 readlines()
with open('') as f:
    content = f.readlines()
    print(content)#reads eachline to a list and ends it with /n

#2 readline()
with open('') as f:
    content = f.readline()
    print(content)#reads one line at a time if you call it agin it wil;l call the second line



with open('') as f:
    content = list(f)
    print(content)#turns eachline  into a list

#iterate over a file\
with open('') as f:
    for line in f:
        print(line,end ="")#end overides the /n



########writing to a file\
with open ('','a') as f:
    f.write("writing some text to the file /n")
    f.write("writing more text")

with open ('','r+') as f:# when using r+ the file must already exist, otherwise you will get an error
    #will both read and write to a file
    f.write("writing some text to the file r+/n") #adds content to the begining of the file
    f.write("writing more text")