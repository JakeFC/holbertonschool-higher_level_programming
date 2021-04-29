#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("")
        return
    for i in range(len(matrix)):
        for n in range(len(matrix[i]) - 1):
            print("{:d} ".format(matrix[i][n]), end="")
        if len(matrix[i]):
            print("{:d}".format(matrix[i][n + 1]), end="")
        print("")
