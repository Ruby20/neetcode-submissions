class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi source BFS

        rows, cols = len(grid), len(grid[0])

        fresh = 0
        time = 0

        # get all the fresh and rotten orange accounting
        que = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    que.append((i, j))

        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        while que and fresh > 0:
            for i in range(len(que)):
                r, c = que.popleft() 
                
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if ( min(row,col) < 0 or
                        row == rows or col == cols or
                        grid[row][col] != 1):
                        continue
                    if grid[row][col] == 1:
                        grid[row][col] = 2
                        que.append((row, col))
                        fresh -= 1
            time += 1
    
        return time if fresh == 0 else -1
        