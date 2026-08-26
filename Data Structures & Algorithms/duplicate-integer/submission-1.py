class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False        

        # time: O(N log N)
        # Space: O(1)