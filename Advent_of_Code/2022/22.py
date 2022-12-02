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
    #print(a, b)
    if b == "Y":
        tot += d[P[R.index(a)]]
        tot += 3
    if b == "X":
        tot += d[P[R.index(a)-1]]
    if b == "Z":
        tot += 6
        tot += d[P[(R.index(a)+1) % 3]]
    #print(tot)
print(tot)