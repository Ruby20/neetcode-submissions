class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        m = len(s)
        n = len(p)

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i >= m and j >= n:
                return True

            if j >= n: # we have reached the end of pattern
                return False

            # we found a single char match
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')    
            
            # Now we have 2 decisions with the * 0 or more occurence match
            if j + 1 < n and p[j + 1] == '*':
                memo[(i, j)] = (match and dfs(i + 1, j)) or dfs(i, j + 2)
                return memo[(i, j)]

            if match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
            memo[(i, j)] = False
            return memo[(i, j)]
        return dfs(0, 0)





