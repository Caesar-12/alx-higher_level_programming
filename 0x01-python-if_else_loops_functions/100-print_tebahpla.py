#!/usr/bin/python3
start = 122
for i in range(0, 26):
    print("{:s}".format(chr(start)), end="")
    if (i % 2) == 0:
        start -= 32
    else:
        start += 32
    start -= 1
