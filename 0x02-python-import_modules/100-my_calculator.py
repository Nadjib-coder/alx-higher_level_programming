#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        if argv[2] != (add or sub or mul or div):
            print("Unknown operator. Available operators: +, -, * and /")
        else:
            a = int(argv[1])
            b = int(argv[3])
            if argv[2] == "+":
                print('{} + {} = {}'.format(a, b, add(a, b)))
            elif argv[2] == "-":
                print('{} - {} = {}'.format(a, b, sub(a, b)))
            elif argv[2] == "*":
                print('{} * {} = {}'.format(a, b, mul(a, b)))
            else argv[2] == "/":
                print('{} / {} = {}'.format(a, b, div(a, b)))
