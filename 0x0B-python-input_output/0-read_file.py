#!/usr/bin/python3
"""creat read_file function"""


def read_file(filename=""):
    """reads filename"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
