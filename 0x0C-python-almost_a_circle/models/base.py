#!/usr/bin/python3
"""
Class Base
"""

import json


class Base:
    """Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return json string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save file to json"""
        new_list = []
        if list_objs is not None:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))

        file = cls.__name__ + ".json"
        with open(file, "w") as f:
            f.write(cls.to_json_string(new_list))
