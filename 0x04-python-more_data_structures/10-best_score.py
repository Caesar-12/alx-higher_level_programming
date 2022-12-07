#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    keys = sorted(a_dictionary.keys())
    largest = 0
    for key in keys:
        if a_dictionary[key] > largest:
            largest = a_dictionary[key]
            largest_key = key
    return largest_key
