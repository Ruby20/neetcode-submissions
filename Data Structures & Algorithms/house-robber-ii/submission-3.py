class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # first and last homes are neighbors - circular
        # we need a flag to tell us about 1 and last
        memo = {}

        def dfs(i, flag):
            if (i, flag) in memo :
                return memo[(i, flag)]
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
                # If i == 0, the first house has been robbed, so flag becomes True.
# The flag remains True for all subsequent calls, ensuring the last house is skipped if reached.
            memo[(i, flag)] = max(dfs(i + 1, flag), dfs(i + 2, flag or (i == 0)) + nums[i])
            return memo[(i, flag)]

        return max(dfs(0, True), dfs(1, False))    


        