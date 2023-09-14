#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    l_ord = list(a_dictionary.keys())
    l_ord.sort()
    for x in l_ord:
        print("{}: {}".format(x, a_dictionary.get(x)))
