#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_c = len(sys.argv) - 1
    if arg_c > 1:
        print("{:d} arguments:".format(arg_c))
    else:
        print("{:d} argument.".format(arg_c))

    for i in range(1, arg_c + 1):
        print("{:d}: {:s}".format(i, sys.argv[i]))
