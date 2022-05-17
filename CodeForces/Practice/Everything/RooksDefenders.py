import sys
from collections import *

sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def bns(low, high,arr):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] >= low and arr[mid] <= high:
            return True
        if arr[mid] < low:
            l = mid + 1
        elif arr[mid] > high:
            r = mid - 1

    return False

def bns2(x,arr):
    l, r = 0, len(arr)-1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1

    return -1

#Binary search for lower bound
def lb(a, x):
    l, r = 0, len(a)-1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] > x:
            ans = mid
            r = mid-1
        else:
            l = mid + 1
    return ans

def solve(n, q, quer):
    row = [0 for _ in range(n+1)]
    col = [0 for _ in range(n+1)]
    freeRow = {i for i in range(n+1)}
    freeCol = {i for i in range(n+1)}
    #print(quer)
    for i  in range(q):
        #print(row, col)
        #print(i)
        #print(freeRow, freeCol)
        if quer[i][0] == 1:
            t, r, c = quer[i]
            row[r] += 1
            col[c] += 1
            if row[r] == 1:
                freeRow.remove(r)
            if col[c] == 1:
                freeCol.remove(c)
        elif quer[i][0] == 2:
            t, r, c = quer[i]
            row[r] -= 1
            col[c] -= 1
            if row[r] == 0:
                freeRow.insert(lb(freeRow,r),r)
            if col[c] == 0:
                freeCol.insert(lb(freeCol,c),c)
        else:
            type, r1,c1, r2, c2 = quer[i]
            if bns(r1, r2, freeRow) and bns(c1, c2, freeCol):
                print("NO")
            else:
                print("YES")


n, q = nl()
quer = []
for _ in range(q):
    quer.append(nl())
solve(n, q, quer)