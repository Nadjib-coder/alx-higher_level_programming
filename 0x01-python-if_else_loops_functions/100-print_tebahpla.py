#!/usr/bin/python3
index = 0
for char in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(char - index)), end="")
    index = 32 if index == 0 else 0
