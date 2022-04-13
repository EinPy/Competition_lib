def getMaxLen(nums):
    n = len(nums)

    if n == 0:
        return 0
    if n == 1:
        if nums[0] > 0: return 1
        else: return 0

    p1 = p2 = best = negs = 0
    lastNeg = -1


    while p2 < n:
        if nums[p2] < 0:
            negs += 1
            if lastNeg == -1:
                lastNeg = p2
        elif not best and nums[p2] > 0:
            best = max(best, 1)

        if nums[p2] != 0:
            if negs % 2 == 0:
                best = max(best, p2 - p1 + 1)
            elif negs % 2 != 0:
                if lastNeg != -1 and lastNeg < p2:
                    best = max(best, p2 - (lastNeg+1) + 1)

        elif nums[p2] == 0:
            p1 = p2 + 1
            negs = 0
            lastNeg = -1

        p2 += 1
    
    return best
        
getMaxLen([1,-2,-3,4])
getMaxLen( [0,1,-2,-3,-4])
getMaxLen([-1,-2,-3,0,1])