import sys
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code

#to pritn a color, a rinter must have at least the required amount of ink
#in all of its color cartridges


def solve(a,b,c):
    C = (a[0],b[0],c[0])
    M = (a[1],b[1],c[1])
    Y = (a[2],b[2],c[2])
    K = (a[3],b[3],c[3])
    P = [C,M,Y,K]


    sum = 0
    colours = [0 for _ in range(4)]


    for c in range(4):
        if sum + min(P[c]) <= 10**6:
            sum += min(P[c])
            colours[c] = min(P[c])
        else:
#            print(sum, 10**6-sum)
            colours[c] = 10**6 - sum
            sum += 10**6 - sum
            

    if sum != 10**6:
        print("IMPOSSIBLE")
    else:
        for el in range(3):
            print(colours[el], end = ' ')
        print(colours[-1])

    


T = int(input())
for case in range(1,T+1):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    print(f'Case #{case}: ', end = '')
    solve(a,b,c)
