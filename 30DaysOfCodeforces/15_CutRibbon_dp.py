import sys
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code


def cut(n,a,b,c,memo, tot = 0):
    cut.c += 1
    if memo[n] != -1:
        return memo[n]
    if n < 0:
        return -1000000
    if n == 0:
        return tot
    ans = max(cut(n-a,a,b,c,memo, tot+1),
    cut(n-b,a,b,c,memo, tot+1),
    cut(n-c,a,b,c,memo, tot+1))
    memo[n] = ans
    return memo[n],
cut.c = 0


n, a, b, c = list(map(int,input().split()))
memo = [-1 for _ in range(n+1)]

print(cut(n,a,b,c, memo), cut.c)