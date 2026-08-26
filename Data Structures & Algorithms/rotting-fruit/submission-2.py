class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs problem
        # multi source BFS 
        # states
            # 0 representing an empty cell
            # 1 representing a fresh fruit
            # 2 representing a rotten fruit
        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1: # fresh
                    fresh += 1
                if grid[r][c] == 2: # rotten
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]            
        
        while fresh > 0 and q:
            qlength = len(q)
            for i in range(qlength):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid)) 
                     and col in range(len(grid[0]))
                     and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -=1
            time += 1

        return time if fresh == 0 else -1                



