#!/usr/bin/python3
""" 2-square.py
Defines a square by 1-square.py
"""


class Square:
    """
    This is a class Square that define a square

    Attributes:
        __size: the int size of square
    """

    def __init__(self, size=0):
        """
        Method __init__ to initialize class

        Parameter:
            size: size of squuare
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
