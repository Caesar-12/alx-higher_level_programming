#!/usr/bin/python3
for i in range(100):
    if i < 99:
        if i <= 9:
            print(f"0{i:d}, ", end="")
        else:
            print(f"{i:d}, ", end="")
    else:
        print(f"{i:d}\n")
