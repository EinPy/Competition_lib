import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code


def solve(n,s1,s2):
    s1.pop(0)
    s2.pop(0)
    f = 0
    while len(s1) > 0 and len(s1) < n and f < 10**6:
        if s1[0] > s2[0]:
            s1.append(s2.pop(0))
            s1.append(s1.pop(0))
        else:
            s2.append(s1.pop(0))
            s2.append(s2.pop(0))
        f += 1
    #not intended solution, however it still workds
    #does not properly determine if lim_f->inf does not yield a winner
    if f == 10**6:
        return -1
    if len(s1) == 0:
        return str(f) + " 2"
    else:
        return str(f) + " 1"



n = int(input())
s1 = list(map(int,input().split()))
s2 = list(map(int,input().split()))
print(solve(n,s1,s2))