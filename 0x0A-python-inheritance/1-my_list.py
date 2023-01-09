#!/usr/bin/python3
"""
Module: 1-my_list
subclass of list that prints list sorted
"""


class MyList(list):

    """
    Class: Mylist
    subclass of list
    """

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
