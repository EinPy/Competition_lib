import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return float(INP())
def nl(): return [float(_) for _ in INP().split()]



arr = []
for _ in range(15):
    l = ni()
    arr.append(abs(l))

for i in range(len(arr)):
    for j in range(len(arr)):
        if max(arr[i], arr[j]) - min(arr[i], arr[j]) < 1.6 and max(arr[i], arr[j]) - min(arr[i], arr[j]) > 1.45:
            print(arr[i],arr[j], max(arr[i], arr[j]) - min(arr[i], arr[j]) )