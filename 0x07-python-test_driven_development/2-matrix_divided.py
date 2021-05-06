#!/usr/bin/python3
"""Module for matrix_divided function
"""


def matrix_divided(matrix, div):
    """Returns a matrix of the original values, divided by div"""
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError('division by zero')
    new = []
    l = len(matrix[0])
    for i in range(len(matrix)):
        row = matrix[i]
        if not isinstance(row, list):
            raise TypeError('matrix must be a matrix (list of lists) of '
                            'integers/floats')
        if len(row) != l:
            raise TypeError('Each row of the matrix must have the same size')
        l = len(row)
        new.append(row.copy())
        for ii in range(l):
            col = new[i][ii]
            if not isinstance(col, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of '
                                'integers/floats')
            new[i][ii] = round(col / div, 2)
    return new
