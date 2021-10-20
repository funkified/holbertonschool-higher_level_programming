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
        return ("[{}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__,
            self.id, self.x, self.y, self.size))

    def uptade(self, *args, **kwargs):
        """ updating class"""
        if args:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.size = j
                if i == 2:
                    self.x = j
                if i == 3:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
