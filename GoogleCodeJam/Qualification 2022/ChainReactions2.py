import sys

sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)
#code


#Sor of right idea, but not correct execution
#needed to implement another base case, and find the value of all 
#possible branches, and memoization
def bfsRec(revG,Ff,S, best = 0):
    best = max(best, Ff[S])
    if revG[S] == []:
        return best

    q = [S]

    while q:
        q2 = []
        for node in q:
            print(node)
            if len(revG[node]) == 1:
                best = max(best,Ff[revG[node][0]])
                q2.append(revG[node][0])
            elif len(revG[node]) > 1:
                alts = []
                for neighbour in revG[node]:
                    alts.append(bfsRec(revG,Ff,neighbour))
                sum = 0
                print(alts)
                for option in alts:
                    sum += option
                sum -= min(alts)
                sum += best
                print(sum)
                return sum
        q = q2

    return best

def solve(n,graph,Ff):

    revG = [[] for _ in range(n)]
    starts = [False for _ in range(n)]
    for node in range(n):
        if graph[node] == 0:
            starts[node] = True
        else:
            revG[graph[node]-1].append(node)

#    print(graph)
#    print(starts)
    print(revG)
    tot = 0
    for node in range(n):
        if starts[node]:
            tot += bfsRec(revG, Ff, node)
    print(tot)


T = int(input())
for case in range(1,T+1):

    n = int(input())
    Ff = list(map(int,input().split()))
    graph = list(map(int,input().split()))

    print(f'Case #{case}: ', end = '')
    solve(n,graph,Ff)
