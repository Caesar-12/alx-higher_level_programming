#!/usr/bin/python3

"""
Module: 1-write_file
writes to a file
"""


def write_file(filename="", text=""):
    """writes string to a text file"""

    with open(filename, "w", encoding="UTF8") as fd:
        cont = fd.write(text)

    return cont
