class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # brute force DFS
        # time: O(M * N)
        # space: O(M * N)
        rows, cols = len(matrix), len(matrix[0])

        dp = {} # (r, c) => LIP
        def dfs(r, c, prevVal):
            key = (r, c)
            if min(r, c) < 0 or r == rows or c == cols or matrix[r][c] <= prevVal:
                return 0

            if key in dp:
                return dp[key]    
            
            res = 1
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]    
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                res = max(res, 1 + dfs(row, col, matrix[r][c]))
            dp[key] = res
            return res
        
        res = float("-inf")
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c, -1))
        return res




