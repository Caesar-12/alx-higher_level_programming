#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    keys = sorted(a_dictionary)

    for key in keys:
        new_dict[key] = (a_dictionary[key] * 2)

    return new_dict
