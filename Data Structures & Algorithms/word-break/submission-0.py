class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp problem
        # Bottom up DP
        dp = [False] * (len(s) + 1)

        dp[len(s)] = True


        for i in range(len(s) - 1, -1, -1):
            for wd in wordDict:
                if (i + len(wd)) <= len(s) and s[i: i + len(wd)] == wd:
                    dp[i] = dp[i + len(wd)]
                if dp[i]:
                    break  
        return dp[0]              
