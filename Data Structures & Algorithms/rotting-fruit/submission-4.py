class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        fresh = 0
        q = collections.deque()
        time = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if  grid[i][j] == 2:
                    q.append((i, j))   

        dirs = [[0, 1],[0, -1],[1, 0], [-1, 0]]

        while fresh > 0 and q:
            # bfs
            for _ in range(len(q)):
                row, col = q.popleft() 
                for dr, dc in dirs:
                    nr = row + dr
                    nc = col + dc
                    #  check for out of bounds
                    if (min(nr, nc) < 0 or nr == rows or nc == cols or grid[nr][nc]!= 1):
                        continue
                    if grid[nr][nc] == 1:    
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            time += 1            
               

        return time if fresh == 0 else - 1