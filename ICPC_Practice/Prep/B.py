
C, n = [int(x) for x in input().split()]
curr = 0
fail = False
for i in range(n):
    left, entered, wait = [int(x) for x in input().split()]
    
    if left > curr:
        fail = True
        break
    
    curr += entered
    curr -= left

    if curr < C and wait != 0:
        fail = True
        break
    if curr > C:
        fail = True

    if left < 0 or entered < 0 or wait < 0:
        fail = True
        break
    if curr < 0:
        fail = True
        break
    if curr > C:
        fail = True
        break
    if curr + wait <= C and wait > 0:
        fail = True
        break
    
    if i == n-1:
        if wait != 0:
            fail = True
            break
        if curr != 0:
            fail = True
            break
    


if fail or curr != 0 or wait != 0:
    print('impossible')
else:
    print('possible')
    
    
