#!/usr/bin/python3

"""
Module: 100-matrix_mul
Multiplies 2 matrix
"""

import numpy

def lazy_matrix_mul(m_a, m_b):
    
    """
    Fuction: matrix_mul
    Matrix multiplication
    """


    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    elif type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0 or (not m_a[0]):
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0 or (not m_b[0]):
        raise ValueError("m_b can't be empty")

    fmat_row = len(m_a)
    smat_row = len(m_b)
    fmat_col = len(m_a[0])
    smat_col = len(m_b[0])

    for item in m_a:
        if type(item) is not list:
            raise TypeError("m_a must be a list of lists")

        if len(item) != fmat_col:
            raise TypeError("each row of m_a must be of the same size")

        for nums in item:
            if not isinstance(nums, int) or not isinstance(nums, int):
                raise TypeError("m_a should contain only integers or floats")

    for item in m_b:
        if type(item) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(item) != smat_col:
            raise TypeError("each row of m_b must be of the same size")
        for nums in item:
            if not isinstance(nums, int) or not isinstance(nums, int):
                raise TypeError("m_b should contain only integers or floats")

    if fmat_col != smat_row:
        raise ValueError("m_a and m_b can't be multiplied")

    mul_list = numpy.dot(m_a, m_b)
    return mul_list
