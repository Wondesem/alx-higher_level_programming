#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum1 = 0
    for i in range(len(sys.argv) - 1):
        sum1 += int(sys.argv[i + 1])
    print("{}".format(total))
