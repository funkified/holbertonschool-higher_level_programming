#!/usr/bin/python3
"""
Task: 4-square
"""


class Square:
    """
    Square class
    Atributte:
        __size: private instance
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an int")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        Property that gets the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter: size for setting value
        """
        if type(value) is int:
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Method to calculate the area of square
        """
        return self.__size ** 2
