#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    number = 0
    denn = 0
    for tupp in my_list:
        number += tupp[0] * tupp[1]
        denn += tupp[1]
    return number / denn
