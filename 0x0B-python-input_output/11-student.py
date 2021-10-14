#!/usr/bin/python3
"""
TASK 11
"""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """Initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to_json """
        if type(attrs) is list:
            new_dict = {}
            for i in attrs:
                if type(i) is str and i in self.__dict__.keys():
                    new_dict[x] = self.__dict__.get(i)
                return new_dict
            else:
                return self.__dict__

    def reload_from_json(self, json):
        """reload_from_json"""
        list_keys = list(json.keys())
        for j in  list_keys:
            self.__dict__[j] = json.get(j)
