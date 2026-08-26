class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # boolean return val expected
        # set is a good DS to eval if num appears more than once
        return len(nums) != len(set(nums))