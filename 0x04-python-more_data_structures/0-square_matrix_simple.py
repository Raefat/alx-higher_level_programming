#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqrt_matrix = []
    for i in range(len(matrix)):
        sqrt_matrix.append([])
        for j in range(len(matrix[i])):
            sqrt_matrix[i][j] = matrix[i][j] ** 2
    return sqrt_matrix
