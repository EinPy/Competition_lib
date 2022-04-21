import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]




# Function to return the count of same pairs
def pair_count(d):
    return sum((i*(i-1))//2 for i in d.values())
  
def Difference(array, m):
      
    # Dictionary changed will store strings 
    # with wild cards
    # Dictionary same will store strings 
    # that are equal
    changed, same = {}, {}
      
    # Iterating for all strings in the given array
    for s in array:
          
        # If we found the string then increment by 1 
        # Else it will get default value 0
        same[s]= same.get(s, 0)+1
          
        # Iterating on a single string
        for i in range(m):
            # Adding special symbol to the string
            t = s[:i]+'#'+s[i + 1:]
              
            changed[t]= changed.get(t, 0)+1
  
    # Return counted pairs - equal pairs
    return pair_count(changed) - pair_count(same)*m


t = ni()
for c in range(t):
    n = ni()
    arr = [None for _ in range(n)]
    for case in range(n):
        s = INP()
        arr[case] = s
    print(Difference(arr,2))

            
        
