#leetcode solution to https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        
        arr = [0 for _ in range(n)]
        
        curMaxL, curMaxR = 0, 0
        lp, rp = 0,n-1
        
        water = 0
        while lp < rp:
            curMaxL = max(curMaxL, height[lp])
            curMaxR = max(curMaxR, height[rp])
            arr[lp] = curMaxL
            arr[rp] = curMaxR
            
            h = min(curMaxL,curMaxR)
            if height[lp] > height[rp]:
                ans2 = h - height[rp-1]
                if ans2 > 0: water += ans2
                rp -= 1
            else:
                ans1 = h - height[lp+1]
                if ans1 > 0: water += ans1
                lp += 1
                
                
        return water
    
