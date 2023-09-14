#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    _ord = list(a_dictionary.keys())
    _ord.sort()
    for x in _ord:
        print("{}: {}".format(i, a_dictionary.get(x)))
