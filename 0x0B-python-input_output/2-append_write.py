#!/usr/bin/python3
"""
Module: 2-append_write
Appends data
"""


def append_write(filename="", text=""):
    """writes string to a text file"""

    with open(filename, "a", encoding="UTF8") as fd:
        cont = fd.write(text)

    return cont
