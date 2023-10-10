#!/usr/bin/python3
"""a module for Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a subclass representing a rectangle"""
    def __init__(self, width, height):
        """a constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """a method thatreturns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """a string representation method"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
