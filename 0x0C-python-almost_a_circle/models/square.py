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

    def uptade(self, *args, **kwargs):
        """ updating class"""
        len_args = len(args)
        if len_args > 0:
            self.id = args[0]
            if len_args > 1:
                self.size = args[1]
                if len_args > 2:
                    self.x = args[2]
                    if len_args > 3:
                        self.y = args[3]
        elif kwargs is not None:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs["x"]
            if 'y' in kwargs:
                self.y = kwargs['y']

