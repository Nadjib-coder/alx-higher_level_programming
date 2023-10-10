#!/usr/bin/python3
"""module for baseGeometry class"""


class BaseGeometry:
    """A BaseGeometry class"""
    def area(self):
        """method to raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a method for validating the value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
