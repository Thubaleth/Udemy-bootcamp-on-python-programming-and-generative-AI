"""
Consider the following string declaration which is part of the output of a Linux command.

my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'

Write a Python script that extracts the MAC address (b4:6d:83:77:85:f3) from the string.

Try to solve the challenge in more than one way.
"""

my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'

mac_adress = my_str[-17:]
print(mac_adress)

#solution 2

mac = my_str.split()
print(mac[-1])