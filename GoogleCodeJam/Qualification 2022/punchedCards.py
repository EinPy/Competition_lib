import sys
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code

#draw R*C matrix without top-left cell

#        +-+
#a cell: |.|
#        +-+



def solve(row, col):
    art = [['.' for _ in range(2*col+1)] for _ in range(2*row+1)]
    for r in range(2*row+1):
        for c in range(2*col+1):
            if r%2 != 0:
                if c%2 == 0:
                    art[r][c] = '|'
            else:
                if c%2 != 0:
                    art[r][c] = '-'
                else:
                    art[r][c] = '+'
    art[0][0], art[0][1], art[1][0], art[1][1] = '.','.','.','.'
    for line in art:
        for char in line:
            print(char,end='')
        print()
                        

    


T = int(input())
for case in range(1,T+1):
    R, C = list(map(int,input().split()))
    print(f'Case #{case}:')
    solve(R,C)
