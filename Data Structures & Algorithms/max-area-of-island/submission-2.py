class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        visit = set()
        def dfs(r, c):
            # base case
            if (min(r, c) < 0 or
                r == rows or c == cols or
                grid[r][c] == 0 or
                (r, c) in visit):
                return 0

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            visit.add((r, c))
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area    


        max_area = 0
        area = 0    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = dfs(r, c)
                    max_area = max(area, max_area)        
        return max_area
        