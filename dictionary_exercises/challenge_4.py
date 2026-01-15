""""
Considering the following dict, get a dict representation sorted by key.

d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}

A dict representation means viewing or printing the dict.



d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}

sorted_dict = dict(sorted(d1.items()))

print(sorted_dict)
"""
#==============================================================
d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
new_dict = sorted(d1.keys())
sorted_dict = {}

for key in new_dict:
    sorted_dict[key] = d1[key]

print(sorted_dict)


