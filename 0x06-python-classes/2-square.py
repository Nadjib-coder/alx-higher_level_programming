#!/usr/bin/python3
"""Definition of  a class Square."""


class Square:
    """Representation of a square."""

    def __init__(self, size=0):
        """Initialization of a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("the size must be an integer")
        elif size < 0:
            raise ValueError("the size must be >= 0")
        self.__size = size
