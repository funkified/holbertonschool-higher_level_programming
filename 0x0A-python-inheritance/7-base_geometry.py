#!/usr/bin/python3
"""
Task 7
"""


class BaseGeometry:
    """
    BaseGeometry
    """
    def area(self):
        """ raise Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate  interger value
        """
        if type(value) is not int:
            raise TypeError("{} must be integer".format(name))
        if value <= 0:
            raise ValueError("{} nust be greater than 0".format(name))
