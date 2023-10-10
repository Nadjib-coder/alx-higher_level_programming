#!/usr/bin/python3
"""lookup method."""


def lookup(obj):
    """lookup object attribute and methods.
    Args:
        obj (object): the object to list.

    Return:
        list: the list of the attibutes.
    """
    return dir(obj)
