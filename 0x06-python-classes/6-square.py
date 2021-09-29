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
        self.size = size
        self.position = position

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
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for idx in range(self.__size):
                    print("#", end="")
                print()

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
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Property
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter method """
        if type(value) is tuple and len(value) == 2 and\
           type(value[0]) is int and type(value[1]) is int and\
           value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
