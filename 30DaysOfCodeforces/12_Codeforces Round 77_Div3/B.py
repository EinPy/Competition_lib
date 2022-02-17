import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#5
def solve(a):
    a, b, c = a
    if a == b == c:
        return "YES"
    diff1 = abs((c-a))/2
    if c!=a and a % diff1 == 0:
        return "YES"
    if c == a:
        if a % c == 0 or c%a == 0:
            return "YES"
    diff2 = abs(b-c)
    if c % diff2 == 0 or diff2 % c == 0:
        return "YES"
    diff3 = abs(c-b)
    if a % diff3 == 0 or diff3 % a == 0:
        return "YES"
    else:
        return "NO"    
    
    
def solve2(arr):
    a, b, c = arr
    if a == b == c:
        return "YES"
    #case multiply a
    diff1 = c-b
    t = b - diff1
    if t >= a:
        if t%a == 0:
            return "YES"
    #case multiply b, a= c
    if a == c:
        if b<= a and a % b == 0:
            return "YES"
    #case multiply b, a!=c
    diff2 = (c-a)/2
    if abs(c-a) % 2 == 0:
        t = a + diff2
        if t >= b:
            if t% b == 0:
                return "YES"
    #case m c
    diff3 = b-a
    t = b + diff3
    if t% c == 0:
        if t >= c:
            return "YES"
    return "NO"
    
    

T = int(input())
for i in range(T):
    a = list(map(int,input().split()))
    print(solve2(a))
    