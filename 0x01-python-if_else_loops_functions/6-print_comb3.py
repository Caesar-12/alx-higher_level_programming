#!/usr/bin/python3
for i in range(9):
    for j in range(i+1,10):
        if i != 8:
            print(f"{str(i):s}{str(j):s}, ", end="")
        else:
            print(f"{i:d}{j:d}")
