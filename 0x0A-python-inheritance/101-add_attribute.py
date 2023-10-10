#!/usr/bin/python3
"""a modulr that defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """add a new attribute to an object
    Args:
        obj (any): the object to add an attribute
        att (str): the name of the attribute to add
        value (any): the value of attribute
    Raises:
        TypeError: if the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
