#!/usr/bin/python3
def append_write(filename="", text=""):
    """writes string to a text file"""

    with open(filename, "a", encoding="UTF8") as fd:
        cont = fd.write(text)

    return cont
