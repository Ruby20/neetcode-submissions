class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state -> Buy/Sell
        # buy i + 1
        # sell i + 2
        memo = {}

        def dfs(i, buying):
            if (i, buying) in memo:
                return memo[(i, buying)]
            if i >= len(prices):
                return 0
            cooldown = dfs(i + 1, buying)    
            if buying:
                # next state is not buying
                # subtract from the profit
                buy = dfs(i + 1, not buying) - prices[i]
                memo[(i, buying)] = max(buy, cooldown)
            else:
                sell = prices[i] +  dfs(i + 2, not buying) 
                memo[(i, buying)] = max(sell, cooldown)
            return memo[(i, buying)]   

        return dfs(0, True)    
        