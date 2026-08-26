class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # order does not matter
        # need uniq combs
        memo = {}

        def dfs(i, target):
            if (i, target) in memo:
                return memo[(i, target)]

            if target == amount:
                memo[(i, target)] = 1
                return 1
            if i >= len(coins)  or target > amount:
                return 0
            memo[(i, target)] =  dfs(i, target + coins[i]) + dfs(i + 1, target)

            return memo[(i, target)]

        return dfs(0, 0)    

        
        
        
        
        

        