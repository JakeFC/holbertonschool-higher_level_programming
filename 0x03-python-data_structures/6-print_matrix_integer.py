#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for i in range(len(matrix)):
        for n in range(len(matrix[i]) - 1):
            print("{:d} ".format(matrix[i][n]), end="")
        if len(matrix[i]):
            if len(matrix[i]) == 1:
                n = -1
            print("{:d}".format(matrix[i][n + 1]), end="")
        print("")
