class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visit = set()

        return self.countDFS(0, 0, grid, visit)

    def countDFS(self, r, c, grid, visit):
        rows, cols = len(grid), len(grid[0])

        # base cases
        if (r < 0 or c < 0  or r == rows or c == cols
            or grid[r][c] == 1 or (r,c) in visit):
            return 0

        # we reached bottom right
        if r == rows-1 and c == cols -1:
            return 1

        visit.add((r,c))

        count = 0
        # recursively move through the matrix
        count += self.countDFS(r,c-1, grid, visit)        
        count += self.countDFS(r,c+1, grid, visit)
        count += self.countDFS(r+1,c, grid, visit)                
        count += self.countDFS(r-1,c, grid, visit)                

        visit.remove((r,c)) # to help with backtracking for multiple path traversal

        return count


        

