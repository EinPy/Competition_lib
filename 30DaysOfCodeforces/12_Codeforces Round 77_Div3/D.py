import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)



def solve(n, k, s):
    if k == n:
        return k
    cnt = {}
    for c in s:
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1
    print(cnt)

T = int(input())
for i in range(T):
    n, k= list(map(int,input().split()))
    s = str(input())
    print(solve(n,k,s))
    