import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,s):
    if n > len(s):
        print("YES")
        return

    num_operations = 0
    # Initialize the current substring that we are trying to match
    curr_substring = []
    d = {}
    s = list(s)
    i = 0
    #print(s)
    while i < n:
        #print(i, curr_substring, num_operations, d)
        if s[i] not in d:
            curr_substring.append(s[i])
            
            num_operations += 1
            d[s[i]] = [i]
            i += 1
        else:
            #print("here")
            bestEnd = -1
            bestS = -1
            for start in d[s[i]]:
                for j in range(min(len(curr_substring)- start, n -i)):
                    if s[i+j] == curr_substring[start + j]:
                        if j > bestEnd:
                            bestEnd = j
                            bestS = start
                    else:
                        break
            curr_substring += curr_substring[bestS:bestS + bestEnd+1]
            for idx in range(i+1,len(curr_substring)):
                if idx < n:
                    d[curr_substring[idx]].append(idx)
            num_operations += 1
            i += bestEnd +1
    #print(curr_substring)
    if num_operations < n:
        print("YES")
    else:
        print("NO")
        
t = ni()
for case in range(t):
    n = ni()
    a = INP()
    solve(n,a)