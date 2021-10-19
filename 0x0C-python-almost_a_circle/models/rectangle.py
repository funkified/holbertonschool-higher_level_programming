#!/usr/bin/python3
"""Task 1"""

from models.base import Base

class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def  __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    @property
    def width(self):
        """width property"""
        return self.__width

    @property
    def height(self):
       return self.__height

    @property
    def x(self):
        """ y property"""
        return self.__x

    @property
    def y(self):
        """y property """
        return self.__y

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an intger")
        if value < 0:
            raise ValueError("width must be greater than 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ sets the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be greater than 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ set x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be greater than 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be greater than 0")
        self.__y = value

    def area(self):
        """area"""
        return self.__height * self.__width

    def display(self):
        """ display """
        print('\n' * self.y, end="")
        print((" " * self.x + ('#' * self.width) + '\n') * self.height, end="")

    def update(self, *args):
        """update args"""
        count = len(args)
        if count > 0:
            self.id = args[0]
            if count > 1:
                self.width = args[1]
                if count > 2:
                    self.height = args[2]
                    if count > 3:
                        self.x = args[3]
                        if count > 4:
                            self.y = args[4]
