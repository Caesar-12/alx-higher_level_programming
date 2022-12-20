#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    numbers = 0
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end="")
        except IndexError:
            print()
            return numbers
        else:
            numbers += 1

    print()
    return numbers
