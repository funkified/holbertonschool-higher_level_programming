#!/usr/bin/python3
"""
Class Base
"""

import json
import csv

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
            return []
        return json.dumps(list_dictionaries)
