#!/usr/bin/python3
"""a Module for Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a subclass representing a rectangle"""
    def __init__(self, size):
        """a constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """a method for area of square"""
        return self.__size ** 2

    def __str__(self):
        """ return string representation of this square"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
