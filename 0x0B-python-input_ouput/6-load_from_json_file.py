#!/usr/bin/python3
"""
Task 6
"""

import json


def load_from_json_file(filename):
    """
    Load from Json file
    """
    with open(filename, 'r', encoding='utf8') as f:
        return json.load(f)
