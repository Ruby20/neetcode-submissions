class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        visit = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0

        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visit:
                    islands += 1
                    self.dfs(i,j,grid,visit)
        return islands            




    def dfs(self, r, c, grid, visit):
        rows, cols = len(grid), len(grid[0])
        # base case 
        if (min(r,c) < 0 or r == rows or c == cols or
            grid[r][c] == "0" or (r,c) in visit):
            return
        
        visit.add((r,c))    
        # recursively find the land
        self.dfs(r, c+1, grid, visit)
        self.dfs(r, c-1, grid, visit)
        self.dfs(r+1, c, grid, visit)
        self.dfs(r-1, c, grid, visit)

        