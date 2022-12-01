#!/usr/bin/python3
import sys

arg_c = len(sys.argv)
if arg_c > 1:
    print("{:d} arguments:".format(arg_c - 1))
else:
    print("{:d} argument:".format(arg_c - 1))

for i in range(1, arg_c):
    print("{:d}: {:s}".format(i, sys.argv[i]))
