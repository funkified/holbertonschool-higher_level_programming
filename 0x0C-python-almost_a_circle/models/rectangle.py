#!/usr/bin/python3
"""
Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width property"""
        return self.__width

    @property
    def height(self):
        """ height"""
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
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height self"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """ display rectanglewith '#' char """
        for i in range(self.height):
            print('#' * self.__width)

    def __str__(self):
        """
        func to override return a  str
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def display(self):
        """ display rectanglewith '#' char """
        print('\n' * self.__y, end="")
        print((' ' * self.__x +
              ('#' * self.__width) + '\n') * self.height, end='')

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
