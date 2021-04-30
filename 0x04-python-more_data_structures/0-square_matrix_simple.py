#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    return [[i * i for i in row] for row in matrix]
