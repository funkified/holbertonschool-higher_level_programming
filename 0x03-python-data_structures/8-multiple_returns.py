#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    return (size, sentence[0] if size > 0 else None)
