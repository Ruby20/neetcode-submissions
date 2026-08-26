class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        cur_min = float("inf")


        while l <= r:
            mid = (l+r)//2
            cur_min = min(nums[mid], cur_min)

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1


        return min(cur_min, nums[l])    
