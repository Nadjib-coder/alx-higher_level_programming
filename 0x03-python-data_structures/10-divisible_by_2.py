#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mult = []
    for i in range(len(my_list) - 1):
        if (my_list[i] % 2) == 0:
            mult[i].append(true)
        else:
            mult[i].append(false)
    return mult
