import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]




t = ni()
for case in range(t):
    n = ni()
    digs = 0
    i = 1
    while i <= n:
        if str(i).count("0") == len(str(i)) - 1:
            digs += 1
            i += 1
        else:
            if str(i)[0] == "9":
                #print(i)
                a = list(str(i))
                a[0] = "0"
                a = ["1"] + ["0"] * (len(a))
                i = int("".join(a))
                #print(a)
            else:
                a = list(str(i))
                a = [str(int(a[0]) + 1)] + ["0"] * (len(a)-1)
                i = int("".join(a))
        
    print(digs)