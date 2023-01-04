#!/usr/bin/python3

"""
Module: 5-text_indentation
"""


def text_indentation(text):

    """
    Function: text_indentation
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    idx = 0
    try:
        while text[idx] is not None:
            if text[idx] in (".", "?", ":"):
                print(text[idx])
                print()
                if text[idx + 1] == " ":
                    idx = idx + 2
            else:
                print(text[idx], end="")
                idx += 1
    except IndexError:
        return
