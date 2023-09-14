#!/usr/bin/python3
def uniq_add(my_list=[]):
    _list = set(my_list)
    result = 0
    for x in _list:
        result += x
    return result
