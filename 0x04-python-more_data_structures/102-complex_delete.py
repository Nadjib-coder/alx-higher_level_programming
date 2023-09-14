#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    l_keys = list(a_dictionary.keys())
    for v_dic in l_keys:
        if value == a_dictionary.get(v_dic):
            del a_dictionary[v_dic]
    return a_dictionary
