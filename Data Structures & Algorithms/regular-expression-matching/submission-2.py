class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i >= m and j >= n:
                return True

            if j >= n:
                return False

            # confirm that i is in bounds
            match = i < m and (s[i] == p[j] or p[j] == ".")    

            # * has the highest precedence
            # Two decisions
            # * -> dont't use it (i, j + 2)
            # * -> use it (i + 1, j)
            if j + 1 < n and p[j + 1] == "*":
                # decision - use * 0    or more times
                memo[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return memo[(i, j)]

            # we don't have a * , looking for a match
            if match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
            memo[(i, j)] = False
            return False   
        return dfs(0, 0)    

