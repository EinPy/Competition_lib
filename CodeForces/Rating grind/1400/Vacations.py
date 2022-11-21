import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = nl()
arr = nl()
z = arr.count(0)
s = []
cur = 0
#insight: Start at first 1 or 2, before that it will always be changed backwards
found = False
is1 = False
for i in range(len(arr)):
    if not found:
        if arr[i] == 1 or arr[i] == 2:
            found = True
            if arr[i] == 1:
                is1 = True
    else:
        if arr[i] == 3:
            is1 = not is1
        if arr[i] == 0:
            is1 = False
            found = False
        if arr[i] == 2:
            if is1:
                is1 = not is1
            else:
                z += 1
                found = False
                is1 = False
        if arr[i] == 1:
            if is1:
                z += 1
                found = False
                is1 = False
            else:
                is1 = not is1
print(z)
                