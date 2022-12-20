#!/usr/bin/python3
def safe_print_division(a, b):
    quotient = None
    try:
        quotient = a / b
    except ZeroDivisionError:
        return None
    finally:
        if quotient:
            print("Inside result: {:.1f}".format(quotient))
        else:
            print("Inside result: {}".format(quotient))

    return quotient
