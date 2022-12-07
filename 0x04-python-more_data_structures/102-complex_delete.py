#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = sorted(a_dictionary.keys())
    new_dict = {}

    for key in keys:
        if a_dictionary[key] == value:
            del a_dictionary[key]
        else:
            new_dict[key] = a_dictionary[key]

    return new_dict
