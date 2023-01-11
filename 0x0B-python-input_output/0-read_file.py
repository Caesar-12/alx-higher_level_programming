#!/usr/bin/python3
"""
Module: 0-read_file
Reads a file
"""


def read_file(filename=""):
    """Reads a text file"""

    with open(filename, "r", encoding="UTF8") as fd:
        for data in fd:
            print(data, end="")
