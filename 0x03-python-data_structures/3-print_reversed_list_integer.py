#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        for num in range(len(my_list) - 1, 0, -1):
            print('{:d}'.format(my_list[num]))
