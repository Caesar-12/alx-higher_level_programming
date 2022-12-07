#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is str or roman_string is None:
        return 0

    roman_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    idx = 0
    value = 0

    for r in roman_string:
        if idx == 0:
            value += roman_dict[r]
            idx += 1
            continue
        if roman_dict[r] > roman_dict[roman_string[idx - 1]]:
            if idx == 1:
                value = (roman_dict[roman_string[idx - 1]]) - value
                idx += 1
                continue
            elif idx > 1:

