import sys
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code

        
def solve(word):
    n = len(word)
    arr = [[0 for col in range(n)] for row in range(n)]
    

    
T = int(input())
for case in range(T):
    n = input()
    print(solve(n))