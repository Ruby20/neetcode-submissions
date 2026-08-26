class Solution:
    def rob(self, nums: List[int]) -> int:
        # dfs with memo technique
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            memo[i] = max(dfs(i + 1), nums[i] +  dfs(i + 2))
            return memo[i]      

        return dfs(0)    
        