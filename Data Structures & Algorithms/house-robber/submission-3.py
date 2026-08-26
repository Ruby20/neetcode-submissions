class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            ans = max(dfs(i + 1), dfs(i + 2) + nums[i])
            memo[i] = ans
            return ans        

        return dfs(0)        
        