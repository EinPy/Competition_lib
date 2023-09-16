def trips(nums):
    trips = []
    size = len(nums)
    nums.sort()
    print(nums)
    for i, v in enumerate(nums):
        #potential duplicate
        if i > 0 and v == nums[i-1]:
            continue # skip loop

        p1 = i+1
        p2 = size - 1
        while p1 < p2:
            #print(i, p1, p2)
            tot = v + nums[p1] + nums[p2]
            if tot > 0:
                p2 -= 1
            elif tot < 0:
                p1 += 1
            else:
                trips.append([v, nums[p1], nums[p2]])
                p1 += 1
                while nums[p1] == nums[p1 -1] and p1 < p2: #only need one place to avoid duplicates
                    p1 += 1
    return trips

print(trips([-1,0,1,2,-1,-4]))
#[-4, -1, -1, 0, 1, 2]