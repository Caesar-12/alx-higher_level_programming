#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        last_digit = number % 10
    else:
        pnum = number * -1
        last_digit = pnum % 10
    print("{:d}".format(last_digit), end="")
    return last_digit
