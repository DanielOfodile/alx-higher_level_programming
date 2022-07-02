#!/usr/bin/python3
def print_list_in_reverse(my_list):
    if my_list:
        for i in reversed(my_list):
            print('{:d}'.format(i))
