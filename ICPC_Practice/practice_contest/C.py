import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



N = ni()
a = list(INP())
b = list(INP())
#print(a, b)
if N % 2 == 0:
    if a == b:
        print("Deletion succeeded")
    else:
        print("Deletion failed")
else:
    isSuccess = True
    #print(len(a))
    for i in range(len(a)):
        #print(a[i], b[i])
        if a[i] == b[i]:
            isSuccess = False
    if isSuccess:
        print("Deletion succeeded")
    else:
        print("Deletion failed")