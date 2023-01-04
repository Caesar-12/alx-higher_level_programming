#!/usr/bin/python3

"""
Module: 2-matrix_divided
Divides element in a matrix
"""


def matrix_divided(matrix, div):

    """
    Function: matrix_divided
    Divides elemwnts in a matrix
    """

    new_mtx = []
    row_len = len(matrix[0])
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for lists in matrix:
        row = len(lists)
        newList = []
        if row != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for nums in lists:
            if type(nums) is not int and type(nums) is not float:
                raise TypeError("matrix must be a matrix \
                                (list of lists) of.integers/floats")
            newList.append(nums)
        new_mtx.append(newList)

    for lists in range(len(new_mtx)):
        for num in range(len(new_mtx[lists])):
            new_mtx[lists][num] = round((new_mtx[lists][num] / div), 2)

    return new_mtx
