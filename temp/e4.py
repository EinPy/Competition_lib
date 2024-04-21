import sys
input = sys.stdin.read
from itertools import permutations

class Data:
    def __init__(self, all0=0, all1=0, rec=0):
        self.all0 = all0
        self.all1 = all1
        self.rec = rec

def rec(r_lo, c_lo, r_hi, c_hi):
    ret = Data()
    if r_lo + 1 == r_hi:
        ret.all0 = int(a[r_lo][c_lo] != '0')
        ret.all1 = int(a[r_lo][c_lo] != '1')
        ret.rec = 0
        b[r_lo][c_lo] = a[r_lo][c_lo]
    else:
        size = (r_hi - r_lo) // 2
        r_mid = r_lo + size
        c_mid = c_lo + size

        kvadrati = [[None, None], [None, None]]
        kvadrati[0][0] = rec(r_lo, c_lo, r_mid, c_mid)
        kvadrati[1][0] = rec(r_mid, c_lo, r_hi, c_mid)
        kvadrati[0][1] = rec(r_lo, c_mid, r_mid, c_hi)
        kvadrati[1][1] = rec(r_mid, c_mid, r_hi, c_hi)

        ret.all0 = ret.all1 = 0
        for kvad in range(4):
            ret.all0 += kvadrati[kvad // 2][kvad % 2].all0
            ret.all1 += kvadrati[kvad // 2][kvad % 2].all1
        
        ret.rec = float('inf')
        kvads = [0, 1, 2, 3]
        for perm in permutations(kvads):
            val = (kvadrati[perm[0] // 2][perm[0] % 2].all0 +
                   kvadrati[perm[1] // 2][perm[1] % 2].all1 +
                   kvadrati[perm[2] // 2][perm[2] % 2].rec +
                   kvadrati[perm[3] // 2][perm[3] % 2].rec)
            
            if val < ret.rec:
                ret.rec = val
                best = perm
        
        for r in range(size):
            for c in range(size):
                b[r_lo + (best[0] // 2) * size + r][c_lo + (best[0] % 2) * size + c] = '0'
                b[r_lo + (best[1] // 2) * size + r][c_lo + (best[1] % 2) * size + c] = '1'

    return ret

def main():
    global a, b, n
    n = int(input())
    a = [input().strip() for _ in range(n)]
    b = [[''] * n for _ in range(n)]
    
    print(rec(0, 0, n, n).rec)
    for line in b:
        print(''.join(line))

if __name__ == "__main__":
    main()
