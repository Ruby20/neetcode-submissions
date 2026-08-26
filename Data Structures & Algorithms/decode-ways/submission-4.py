class Solution:
    def numDecodings(self, s: str) -> int:
        # count the number of different ways to decode the string
        dp = {len(s) : 1} # i + 2 or len(s) = 1 for empty string

        for i in range(len(s) - 1, -1, -1):
            if i in dp:
                return dp[i]

            if s[i] == '0':
                dp[i] = 0
            else:    
                dp[i] = dp[i + 1]    
                if (i + 1 < len(s) and (s[i] == '1' or s[i] == '2'
                    and s[i + 1] in '0123456')):
                    dp[i] += dp[i + 2]
                    print(dp[i + 2], dp[i + 1])
                    # print(dp[i], i)
        return dp[0]            

# hus, possible decoding sequences are:

    # Single digits only: 2 5 6 6 7 8 - Single digits btw 1 - 9
    # First two digits as a pair: 25 6 6 7 8 Double digits => 25 only
    # so two ways
        