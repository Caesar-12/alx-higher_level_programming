#!/usr/bin/python3
def read_file(filename=""):
    """Reads a text file"""

    with open(filename, "r", encoding="UTF8") as fd:
        for data in fd:
            print(data, end="")
