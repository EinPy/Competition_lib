import code
import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code
# greedy solution to https://codeforces.com/contest/1418/problem/C
#really fucking big brain solution

def solve(n,bs):
    score = 0
    score += bs[0]
    i = 1
    while i < n:
        if bs[i] == 0:
            i += 1
        else:
            j = i
            while j < n and bs[j] == 1:
                j += 1
    #        print(i,j)
            score += (j-i) // 3
            i = j
    return score
    




T = int(input())
for c in range(T):
    n = int(input())
    bs = list(map(int,input().split()))
    print(solve(n,bs))
