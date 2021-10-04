#!/usr/bin/python3
"""
Create Class: Rectangle
"""


class Rectangle:
    """ Empty Rectangle"""
    def __init__(self, width=0, height=0):
        """init rectangle"""
        self.width = width
        self.height = height

    def __str__(self):
        if self.area() == 0:
            return ""
        return (('#' * self.__width + '\n') * self.__height)[:-1]

    @property
    def height(self):
        """method property"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """method property"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ Calculates area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates perimeter of rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.__height + self.__width)
