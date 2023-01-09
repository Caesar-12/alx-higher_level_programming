#!/usr/bin/python3
"""
module: 3-is_kind_of_class
checks for instances
"""


def is_kind_of_class(obj, a_class):
    """returns true if instance, false otherwise"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
