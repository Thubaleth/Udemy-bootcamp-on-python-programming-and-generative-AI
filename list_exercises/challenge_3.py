#Given the string nums = '10,20,30,40,50', write a Python script that converts it into a list of integers: [10, 20, 30, 40, 50].

nums = "10,20,30,40,50"
new_num = nums.split(",")

new_list = []
for i in new_num:
    new_list.append(int(i))
print(new_list)