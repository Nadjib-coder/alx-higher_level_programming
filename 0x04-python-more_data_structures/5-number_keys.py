#!/usr/bin/python3
def number_keys(a_dictionary):
    result = 0
    list_keys = list(a_dictionary.keys())
    for x in list_keys:
        result += x
    return result
