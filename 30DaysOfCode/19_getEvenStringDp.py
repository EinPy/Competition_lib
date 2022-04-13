import sys
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code

        
def check(s):
    if len(s) %2 != 0:
        return False

    c = 0
    let = "æ"
    for chr in s:
        if chr != let:
            if c % 2 != 0:
                return False
            let = chr
            c = 1
        else:
            c += 1
    return True        
        
        
def rec(s, mem = {}):
    if s in mem:
        return mem[s]
    if check(s):
        return 0
    
    ways = [0 for _ in range(len(s))]
    
    for i in range(len(s)):
        if i == 0:
            newS = s[1:]
        elif i == len(s)-1:
            newS = s[:-1]
        else:
            newS = s[:i] + s[i+1:]
        ans = rec(newS)
        ways[i] = 1 + ans
        
    mem[s] = min(ways)
    return mem[s]
        
    
T = int(input())
for case in range(T):
    n = input()
    print(rec(n))