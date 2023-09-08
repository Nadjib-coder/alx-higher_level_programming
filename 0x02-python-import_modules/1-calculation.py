#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    addition = add(a, b)
    substraction = sub(a, b)
    multiplication = mul(a, b)
    division = div(a, b)
    print("{} + {} = {}".format(a, b, addition))
    print("{} - {} = {}".format(a, b, substraction))
    print("{} * {} = {}".format(a, b, multiplication))
    print("{} / {} = {}".format(a, b, division))
