#!/usr/bin/python3
"""
Task: 5-square
"""


class Square:
    """
    Square Class
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initialize
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Property
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter
        """
        if type(value) is not tuple or \
                len(value) is not 2 or type(value) is not int:
                raise TypeError("position must be a tuple of \
                        2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Method to calculate area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Public Method to print a square with #
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
