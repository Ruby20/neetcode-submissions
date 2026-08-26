class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxarea = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = self.countDFS(r,c,grid,visit)
                    maxarea = max(area, maxarea)

        return maxarea



    def countDFS(self, r, c, grid, visit):
        rows, cols = len(grid), len(grid[0])

        # base cases
        if (r < 0 or c < 0  or r == rows or c == cols
            or grid[r][c] == 0 or (r,c) in visit):
            return 0

        visit.add((r,c))

        
        # recursively move through the matrix
        return 1 + self.countDFS(r,c-1, grid, visit)+self.countDFS(r,c+1, grid, visit)+ self.countDFS(r+1,c, grid, visit)+self.countDFS(r-1,c, grid, visit)   

       
        