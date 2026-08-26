class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 1. brute force approach 
        # run two loops

        # 2. Optimize with Two pointers
        left = 0
        right = len(heights) - 1

        res = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            res = max(res, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1    

        return  res      