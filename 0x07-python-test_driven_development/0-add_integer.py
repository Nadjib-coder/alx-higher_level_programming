#!/usr/bin/python3
"""
This module contains a function to perform integer addition.
Usage:
    from 0-add_integer import add_integer
    result = add_integer(5, 3)
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
