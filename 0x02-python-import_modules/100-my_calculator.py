#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        if sys.argv[2] != (add or sub or mul or div):
            print("Unknown operator. Available operators: +, -, * and /")
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if sys.argv[2] == "+":
                print('{} + {} = {}'.format(a, b, add(a, b)))
            elif sys.argv[2] == "-":
                print('{} - {} = {}'.format(a, b, sub(a, b)))
            elif sys.argv[2] == "*":
                print('{} * {} = {}'.format(a, b, mul(a, b)))
            else sys.argv[2] == "/":
                print('{} / {} = {}'.format(a, b, div(a, b)))
