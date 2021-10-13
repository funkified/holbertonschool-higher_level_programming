#!/usr/bin/python3
"""
Task 11: Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        """ Initialize"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ area of instance """
        return self.__size ** 2

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
