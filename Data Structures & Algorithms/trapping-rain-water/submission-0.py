class Solution:
    def trap(self, height: List[int]) -> int:
        # edge case
        if not height:
            return 0
        l = 0
        r = len(height)-1

        lmax, rmax = height[l], height[r]
        res = 0

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                # add that to the results
                res += (lmax - height[l])
            else:
                r -= 1    
                rmax = max(rmax, height[r])
                # add that to the results
                res += (rmax - height[r])
        return res        

