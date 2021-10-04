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

    @property
    def height(self):
        """method property"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height value"""
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
        """sets the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ calculates the area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """ calculates teh perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.__height + self.__width)
