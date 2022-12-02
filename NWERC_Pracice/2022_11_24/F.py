import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



N = list(map(int,list(INP())))
#print(N)
freq = {}
arr = [0 for _ in range(10)]
for el in N:
    arr[el] += 1



m = 1e9
minIdx = -1
for i in range(len(arr)-1,0,-1):
    if arr[i] <= m:
        m = arr[i]
        minIdx = i
    #print(i)
if arr[0] < m:
    print("1" + "0" * (arr[0] + 1))
else:
    print(str(minIdx) * (arr[minIdx] + 1))
