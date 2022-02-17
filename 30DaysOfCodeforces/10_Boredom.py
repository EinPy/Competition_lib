import sys
sys.setrecursionlimit(10**5)

import sys


def setupInputOutputSublime():
    import os

    if os.name == 'nt':
        sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
        sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
#setupInputOutputSublime()


itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#https://codeforces.com/problemset/problem/455/A

# not for today, look at this https://bruceoutdoors.wordpress.com/2015/11/08/445a-boredom-codeforces-tutorial/


def solve(m):
    dp[0],dp[1] = 0, c[1]
    
    for i in range(2,m+1):
        dp[i] = max(dp[i-1],dp[i-2]+i*c[i])

    return dp[m]


n = int(input())
a = list(map(int,input().split()))
a.sort()
c = [0 for _ in range(1000001)]
m = 0
dp = [None for _ in range(1000001)]
for v in a:
    c[v] += 1
    m = max(m, v)

print(solve(m))

'''
#case 2
max(x.count(1)*1,x.count(2)*2)
#case 3
max(x.count(1)*1 + x.count(3)*3,x.count(2)*2)

when on a number you can reduce it to two cases if you
start at the max
+ f(i-2) + f(i)
+ f(i-1) 
'''