#!/usr/bin/python3
"""
This module contains a function to perform integer addition.
The add_integer module provides a simple function to add two integers.
It also supports casting from floats to integers before performing the addition.
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
