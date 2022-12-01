#!/usr/bin/python3
from sys import argv

result = 0
for num in range(len(argv) - 1):
    result += int(argv[num + 1])

print("{:d}".format(result))
