import sys
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code
print

def cut(n,a,b,c,memo, tot = 0):
#    print(n, a, b, c, memo, tot)
    cut.c += 1
#    print(memo)
    if memo[n] != -1:
#        print(memo[n])
#        print(type(memo[n]))
        print("memo: ", memo[n])
        return memo[n]
    if n < 0:
        return -1000000
    if n == 0:
#        print(type(tot))
        print("here: ", tot)
        return tot
    print(cut(n-a,a,b,c,memo, tot+1))
    print(cut(n-b,a,b,c,memo, tot+1))
    print(cut(n-c,a,b,c,memo, tot+1))
    return memo[n],
cut.c = 0


n, a, b, c = list(map(int,input().split()))
memo = [-1 for _ in range(n+2)]

print(cut(n,a,b,c, memo), cut.c)
print(cut.c)
print(cut.c)