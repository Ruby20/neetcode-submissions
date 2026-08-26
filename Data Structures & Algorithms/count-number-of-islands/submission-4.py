class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs
        rows, cols = len(grid), len(grid[0])
        islands = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def bfs(r, c):
            q = deque()
            grid[r][c] = "0" # mark it as visited
            q.append((r, c))

            while q:
                row, col = q.popleft() 
                for dr, dc in dirs:
                    nr = row + dr
                    nc = col + dc
                    if ((min(nr, nc) < 0) or nr == rows or nc == cols 
                        or grid[nr][nc] == "0"):
                        continue
                    grid[nr][nc] = "0" # mark it as visited
                    q.append((nr, nc))    


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1            


        return islands


