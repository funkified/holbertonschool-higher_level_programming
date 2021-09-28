#!/usr/bin/python3
"""
Task: 5-square
"""


class Square:
    """
    Square Class
    """

    def __init__(self, size=0):
        """
        initialize
        """
        self.__size = size

    @property
    def size(self):
        """
        Property getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter
        """
        if type(value) is int:
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Method to calculate area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Public Method to print a square with #
        """
        for i in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()
