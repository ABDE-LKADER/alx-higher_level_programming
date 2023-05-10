#!/usr/bin/python3
for x in range(0, 100):
    if x < 10:
        print("0{:d}".format(x), end='')
    else:
        print("{:d}".format(x), end='')
    if x < 99:
        print(", ", end='')
