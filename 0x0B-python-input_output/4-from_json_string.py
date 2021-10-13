#!/usr/bin/python3
"""
Task 4: from_json_string
"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python structure) represented by a JSON string
    """
    return json.loads(my_str)
