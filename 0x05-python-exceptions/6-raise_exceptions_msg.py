#!/usr/bin/python3
def raise_exceptions_msg(message=""):
    try:
        raise NameError
    except NameError:
        print(message)
