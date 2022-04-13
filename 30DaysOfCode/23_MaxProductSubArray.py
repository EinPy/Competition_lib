#solution to https://leetcode.com/problems/maximum-product-subarray/


class Solution:
    def maxProduct(self, nums):
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        curMax = maxSub = nums[0]
        curMin = minSub = nums[0]
        
        for i in range(1,n):

           #if the number is negative, when multiplied it will swap the sign
           # of the number it is multiplied with.  
            if nums[i] <0:
                curMax, curMin = curMin, curMax
            
            curMax = max(nums[i], curMax * nums[i])
            maxSub = max(curMax, maxSub)
            
            curMin = min(nums[i], curMin *nums[i])
            minSub = min(curMin, minSub)
            
        
        return maxSub
         
        