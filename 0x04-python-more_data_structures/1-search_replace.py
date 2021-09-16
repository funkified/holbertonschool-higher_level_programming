#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [idx if idx is not search else replace for idx in my_list]
