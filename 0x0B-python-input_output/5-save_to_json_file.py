#!/usr/bin/python3
"""
Task 5
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Functions that writes an objcject to a text file,
    Using JSON representation
    """
    with open(filename, 'w', encoding='utf8') as file:
        json.dump(my_obj, file)
