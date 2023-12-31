#!/usr/bin/python3
"""
This module contains a function to perform integer addition.

The add_integer module provides a simple function to add two integers.
"""


def add_integer(a, b=98):
    """
    this method adds 2 integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

if __name__ = "__main__":
    import doctest
    doctest.testfile("test/0-add_integer.txt")
