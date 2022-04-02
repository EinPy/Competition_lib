import sys
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)
#code

def solve(n, a):
    if n == 1:
        return 1
    a.sort()
    streak = 0
    for num in a:
        if num > streak:
            streak+= 1

    return streak




T = int(input())
for case in range(1,T+1):
    n = int(input())
    a = list(map(int,input().split()))
    print(f'Case #{case}: ', end = '')
    print(solve(n,a))
