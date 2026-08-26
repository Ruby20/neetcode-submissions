class Solution:
    def findMin(self, nums: List[int]) -> int:
        # log n -> binary search
        left = 0
        right = len(nums) - 1
        curmin = float("inf")

        while left <= right:
            mid = left + ((right - left) // 2 ) # overflow handling
            curmin = min(curmin, nums[mid])
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return curmin            

        