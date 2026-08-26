class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c1, c2 = 0, 0

        # [c1, c2, n, n+1, n+2, ....]
        # each step pick min
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1],  cost[i+2] )

        return min(cost[0], cost[1])    