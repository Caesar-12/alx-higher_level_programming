#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        for num in lists:
            print("{:d} ".format(num), end="")
        print()
