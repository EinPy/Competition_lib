import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = ni()
arr = nl()
arr_order = [(arr[i], i) for i in range(n)]
arr.sort(reverse=True)
arr_order.sort(reverse=True)
#print(arr_order)
if sum(arr[1:]) >= arr[0]:
    for v, i in arr_order:
        print(i+1, end = " ")
else:
    print("impossible")
#print(arr_order)