class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height)-1    
        lmax, rmax = height[l], height[r]
        count = 0

        while l < r:
            if lmax < rmax:
                l += 1 # we move the min value ptr
                lmax = max(lmax, height[l])
                count += (lmax - height[l])
            else:
                r -= 1
                rmax = max(rmax, height[r])
                count += (rmax - height[r])
        return count            
                
