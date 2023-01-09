#!/usr/bin/python3
"""
module: 4-inherits_from.py
checks for instances
"""


def inherits_from(obj, a_class):
    """returns true if instance, false otherwise"""

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
