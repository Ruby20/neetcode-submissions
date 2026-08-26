class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * (amount + 1) # assign an array of amount of 1
        dp[0] = 0

        for am in range(1 , amount + 1):
            for c in coins:
                if am - c >= 0:
                    dp[am] = min(dp[am], 1 + dp[am - c])
        return dp[amount] if dp[amount] != (amount + 1) else -1            
        