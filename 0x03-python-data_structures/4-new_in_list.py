#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temp = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return temp
    else:
        temp[idx] = element
        return temp
