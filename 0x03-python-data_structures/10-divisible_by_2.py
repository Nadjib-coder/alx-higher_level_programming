#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mult = []
    for i in range(len(my_list) - 1):
        if (my_list[i] % 2) == 0:
            mult.append(true)
        else:
            mult.append(false)
    return mult
