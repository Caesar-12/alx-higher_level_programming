#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        size = 1
        for num in lists:
            if size < len(lists):
                print("{:d} ".format(num), end="")
            elif size == len(lists):
                print("{:d}".format(num), end="")
            size += 1
        print()
