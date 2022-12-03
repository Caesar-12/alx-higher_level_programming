#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lfl = len(tuple_a)
    lsl = len(tuple_b)
    if tuple_a or tuple_b:
        if lfl >= 2 and lsl >= 2:
            new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        elif lfl >= 2 and lsl == 1:
            new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[0] + 0)
        elif lfl >= 2 and lsl == 0:
            new_tuple = (tuple_a[0] + 0, tuple_a[1] + 0)
        elif lfl == 0 and lsl >= 2:
            new_tuple = (0 + tuple_b[0], 0 + tuple_b[1])
        elif lfl == 1 and lsl >= 2:
            new_tuple = (tuple_a[0] + tuple_b[0], 0 + tuple_b[1])
        elif lfl == 0 and lsl == 0:
            new_tuple = (0, 0)
        elif lfl == 1 and lsl == 1:
            new_tuple = (tuple_a[0] + 0, 0 + tuple_b[0])
        return new_tuple
