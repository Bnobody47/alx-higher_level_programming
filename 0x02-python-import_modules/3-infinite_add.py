#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sume = 0
    for i in range(1, len(sys.argv)):
        sume = sume + int(sys.argv[i])
    print(sume)
