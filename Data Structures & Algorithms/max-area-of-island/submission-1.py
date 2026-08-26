class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # edge cases
        if not grid or not grid[0]:
            return 0

        visit = set()
        # dims
        rows, cols = len(grid), len(grid[0])

        # dfs helper
        def dfs(r, c):
            # check for out of bounds
            if (r not in range(rows)
                or c not in range(cols)
                or (r,c) in visit
                or grid[r][c] == 0 )    :
                return 0

            visit.add((r,c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        maxislands = 0
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    islands = dfs(r,c)
                    maxislands = max(maxislands, islands)
                    
        return maxislands                  


        