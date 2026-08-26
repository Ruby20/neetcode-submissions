class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = sys.maxsize
        maxProfit = 0

        for i in range(len(prices)):
            minPrice = min(prices[i], minPrice)
            maxProfit = max(maxProfit, prices[i]-minPrice)
        
        return maxProfit