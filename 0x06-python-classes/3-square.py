#!/usr/bin/python3
"""
Task: 3-square
"""


class Square:
    """
    Class that defines a square
    Attributes:
        _size: int size of square
    """
    def __init__(self, size=0):
        self.__size = size
    """
    Method to initialize clas
    """

    def area(self):
        """
       Method to calculate area of square
       """
        self.area = self.__size * self.__size
        return self.area
