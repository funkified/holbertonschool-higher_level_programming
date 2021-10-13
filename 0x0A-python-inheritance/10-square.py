#!/usr/bin/python3
"""
Task 10: Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Area of square instance"""
        return self.__size ** 2
