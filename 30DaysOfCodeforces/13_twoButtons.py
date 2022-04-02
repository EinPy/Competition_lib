import code
import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)
#code
#clever application of bfs to do a complete search to solve
#https://codeforces.com/problemset/problem/520/B

def solve(n,m, steps = 0):
    if n == m:
        return steps
    return bfs(n,m)
    
#Bfs to find distannce to all nodes in graph 
def bfs(S, G):
    q = [S]
    #remember that range is notinclusive of end
    dists = [-1 for _ in range((2*10**4)+1)]
    dists[S] = 0
    while q:
        q2 = []
        for u in q:
            for n in [u*2, u-1]:
                if n <= 2 * 10**4 and n > 0:
                    if dists[n] == -1:
                        dists[n] = dists[u] + 1
                        q2.append(n)
                        if n == G:
                            return dists[n]
        q = q2


n, m = list(map(int,input().split()))
print(solve(n,m))