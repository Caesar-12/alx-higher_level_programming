#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arg_c = len(argv) - 1
    if arg_c > 1:
        print("{:d} arguments:".format(arg_c))
    elif arg_c == 1:
        print("{:d} argument:".format(arg_c))
    else:
        print("{:d} arguments.".format(arg_c))

    if arg_c > 0:
        for i in range(1, arg_c + 1):
            print("{:d}: {:s}".format(i, argv[i]))
