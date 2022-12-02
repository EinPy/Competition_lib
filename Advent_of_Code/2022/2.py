import sys
from collections import *
sys.setrecursionlimit(10**5)

tot = 0
for line in sys.stdin.read().strip().split('\n'):
    a, b = line.split()
    d = {}
    d["X"] = 1
    d["Y"] = 2
    d["Z"] = 3
    R = ["A", "B", "C"]
    P = ["X", "Y", "Z"]
    tot += d[b]
    #print(a, b)
    if R.index(a) == P.index(b):
        tot += 3
    elif R.index(a) == P.index(b) + 1 or P.index(b) == 2 and R.index(a) == 0:
        tot += 0
    else:
        tot += 6
    #print(tot)
print(tot)
