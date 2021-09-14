#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for idx, element in enumerate(my_list):
        if idx < 0 or idx > len(my_list) - 1:
            return my_list
        if my_list[idx] == 3:
            my_list[element] = 9
            return my_list
