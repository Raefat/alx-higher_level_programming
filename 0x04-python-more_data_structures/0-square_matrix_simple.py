#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqrt_matrix = matrix.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sqrt_matrix[i][j] = matrix[i][j] ** 2
    return sqrt_matrix
