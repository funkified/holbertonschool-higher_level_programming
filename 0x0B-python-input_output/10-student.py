#!/usr/bin/python3
"""
Module: Class Student
"""


class Student:
    """
    class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        public method tha tretrieves a dictionary
        representation of a studient
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for lstAttrs in attrs:
                if lstAttrs in self.__dict__.keys():
                    new_dict[lstAttrs] = self.__dict__[lstAttrs]
            return new_dict
