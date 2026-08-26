class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        visit = set()
        def dfs(r, c):
            # base case
            if (min(r, c) < 0 or
                r == rows or c == cols or
                grid[r][c] == "0" or
                (r, c) in visit):
                return

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)


        islands = 0    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands            
                    


        