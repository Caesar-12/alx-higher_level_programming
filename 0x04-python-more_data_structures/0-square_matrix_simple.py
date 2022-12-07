#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    # square numbers in list
    for i in range(len(matrix)):
        num_list = []
        for j in range(len(matrix[i])):
            square = matrix[i][j] * matrix[i][j]
            num_list.append(square)
        new_matrix.append(num_list)
    return new_matrix
