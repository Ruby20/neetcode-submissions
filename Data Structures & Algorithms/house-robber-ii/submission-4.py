class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_helper(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                temp = max(rob1, n + rob2)
                rob2 = rob1
                rob1 = temp
            return rob1    

        return max(nums[0], rob_helper(nums[1:]), rob_helper(nums[:-1]))



        