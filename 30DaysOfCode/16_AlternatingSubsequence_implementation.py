from ast import Pass
import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code


def solve(n,a):
    if n == 0:
        return 0
    i = 0
    sum = 0

    if a[i] >0:
        pos = True
    else:
        pos = False

    while i < n:
        if pos:
            curMax = a[i]
            while i+1 < n and a[i+1] > 0:
                i += 1
                curMax = max(curMax, a[i])
            sum += curMax
            pos = False
        else:
            curMax = a[i]
            while i + 1 < n and a[i + 1] < 0:
                i += 1
                curMax = max(curMax, a[i])
            sum += curMax
            pos = True
        i += 1
    print(sum)



T = int(input())
for test in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    solve(n,a)