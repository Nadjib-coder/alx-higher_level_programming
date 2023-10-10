#!/usr/bin/python3
"""a module contains the class MyInt"""


class MyInt(int):
    """rebel of an integer"""
    def __new__(cls, *args, **kwargs):
        """create a new instance"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """__eq__ method"""
        return int(self) != other

    def __ne__(self, other):
        """__ne__ method"""
        return int(self) == other
