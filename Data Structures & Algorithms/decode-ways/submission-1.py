class Solution:
    def numDecodings(self, s: str) -> int:
        # count the number of different ways to decode the string
        cache = {len(s) : 1}
        def dfs(i):
            if i in cache:
                return cache[i]
            # no leading 0s
            if s[i] == '0':
                return  0
            
            # we can consider 1 - 9 for the first branch
            res = dfs(i + 1) # dp[len(s) - 1] = 1

            # second character should be 1 or 2 
            # the third character should be between 0 - 6
            # cannot be 27; has to be between 10 - 26
            if (i + 1 < len(s) and 
                (s[i] == '1' or s[i] == '2' and
                s[i + 1] in '0123456')):
                res += dfs(i + 2)
            cache[i] = res
            return res
        
        return dfs(0)        




        