#!/usr/bin/python3
"""
Task 9: Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle Class
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Calculates area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ string """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
