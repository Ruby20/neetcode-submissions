class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        maxProfit = 0

        for sell in range(len(prices)):
            localProfit = prices[sell] - prices[buy]
            if prices[buy] <= prices[sell]:
                maxProfit = max(maxProfit, localProfit)
            else:
                prices[buy] = prices[sell]

        return maxProfit            