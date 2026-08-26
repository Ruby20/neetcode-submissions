class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # check for valid grid
        if not grid or not grid[0]:
            return 0

        visit = set()
        island_count = 0
        # get the dim
        rows, cols = len(grid), len(grid[0]) 

        # dfs recursive helper
        def dfs(r, c):
        # check for boundaries
            if ( r not in range(rows)
                or c not in range(cols)
                or (r,c) in visit
                or grid[r][c] == "0"):
                return
        
            visit.add((r,c))
            directions = [[0,1],[0, -1],[1, 0], [-1,0]]
            for i,j in directions:
                dfs(r + i, c+j)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    island_count += 1
                    dfs(r,c)
        return island_count            





        





