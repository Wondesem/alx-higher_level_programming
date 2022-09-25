#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum1 = 0
    if len(sys.argv) == 1:
        print("{}".form(sum1))
    else:
    for i in range(1, len(sys.argv)):
        sum1 += int(sys.argv[i])
    print("{}".format(sum1))
