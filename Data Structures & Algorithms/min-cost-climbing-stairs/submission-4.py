class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # You may choose to start at the index 0 or the index 1 floor.
        memo = {}
        def dfs(i):
            if  i >= len(cost):
                return 0
            if i in memo:
                return memo[i]

            memo[i] = min(dfs(i + 1), dfs(i + 2)) + cost[i]
            return memo[i]

        return min(dfs(0), dfs(1))            