#!/usr/bin/python3
'#program that prints all numbers from 0-98 in decimal and hexa '

"""Print numbers 0 to 98 in decimal and hexadecimal."""
for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
