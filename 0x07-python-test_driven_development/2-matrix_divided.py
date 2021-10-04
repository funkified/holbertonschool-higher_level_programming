#!/usr/bin/python3
"""
2-matrix_divided
"""
def matrix_divided(matrix, div):
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of\
                integers/floats")
    for row in matrix:
        size = None
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) of\
                    integers/floats")
        if size is None:
            size = len(row)
        elif size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        if type(div) not in [int, float]:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        return [[round(element / div, 2) for element in row] for row in matrix]
