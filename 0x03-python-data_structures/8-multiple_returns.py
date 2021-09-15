#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    first = sentence[0]
    if sentence == "":
        first = None
    return [size, first]
