#!/usr/bin/python3
"""
Task: 5-square
"""


class Square:
    """Define a Square Class
    """

    def __init__(self, size=0, position=(0, 0)):
        """ initialize and validates given size

        Args:
            size (int): integer greater or equal to zero
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Method to calculate area of square

        Returns:
            int: area of square
        """
        return self.__size ** 2

    def my_print(self):
        """Public Method to print a square with #
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def size(self):
        """Property getter
        Class Instance

        Returns:
            int: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set size of square instance

        Arguments:
        value (int): size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter method
        """
        flag = False
        if type(value) is tuple:
            if len(value) is 2:
                if type(value[0]) is int and value[0] >= 0:
                    if type(value[1]) is int and value[1] >= 0:
                        flag = True
                        self.__position = value
        if flag is False:
            raise TypeError("position must be a tuple of 2 positive integers")
