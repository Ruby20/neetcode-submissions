class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1, w2 = len(word1), len(word2)

        dp = [[float("inf")] * (w2+1) for i in range(w1+1)]
        
        # fill up the extra row/col with the w1 and w2 lens
        for i in range(w2+1):
            dp[w1][i] = w2-i
        for j in range(w1+1):
            dp[j][w2] = w1-j

        for i in range(w1-1, -1, -1):
            for j in range(w2-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:            
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

        return dp[0][0]            



