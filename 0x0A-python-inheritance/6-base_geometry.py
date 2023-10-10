#!/use/bin/python3
""" a module to write a class with public instacne method"""


class BaseGeometry:
    """a BaseGeometry class"""
    def area(self):
        """method to raise an exception"""
        raise Exception("area() is nit implemented")
