#!/usr/bin/python3
"""
Task 7
"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except:
    my_list = []

for i in argv[1:]:
    my_list.append(i)

save_to_json_file(my_list, filename)
