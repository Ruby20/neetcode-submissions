class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dynamic programming
        maxP = 0
        min_price = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - min_price)
            min_price = min(min_price, sell)

        return maxP    


        # # brute force
        # profit = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         profit = max(profit, prices[j] - prices[i])

        # return profit        
                
        