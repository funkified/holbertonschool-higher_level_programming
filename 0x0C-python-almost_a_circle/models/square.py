#!/usr/bin/python3
"""
Module: Class Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        size property = height or width
        """
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width))
