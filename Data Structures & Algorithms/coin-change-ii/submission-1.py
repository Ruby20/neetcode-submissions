class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, target):
            if (i, target) in memo:
                return memo[(i, target)]

            if target == amount:
                return 1
            if i >= len(coins)  or target > amount:
                return 0
            if coins[i] > amount:
                memo[(i, target)] = dfs(i + 1, target)
            else:    
                memo[(i, target)] =  dfs(i, target + coins[i]) + dfs(i + 1, target)

            return memo[(i, target)]

        return dfs(0, 0)    