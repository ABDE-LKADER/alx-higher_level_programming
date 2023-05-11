#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) - 1 == 0:
        print("0 arguments.")
    elif len(sys.argv) - 1 == 1:
        print("1 arguments:")
    else:
        print("{:d} argument:".format(len(sys.argv) - 1))
    for i in range(len(sys.argv) - 1):
        print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
