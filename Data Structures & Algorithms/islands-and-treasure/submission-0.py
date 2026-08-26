class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visit = set()

        # multisource BFS
        def addRoom(r, c):
            # base case
            if (min(r, c) < 0 or
                r == rows or c == cols or
                (r, c) in visit or
                grid[r][c] == -1
                ):
                    return
            visit.add((r, c))        
            q.append([r, c])

        # identify all gates and add to q for BFS     
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        dist = 0
        # modify the cells dist, no return stmt
        while q:
            for i in range(len(q)):
                r, c = q.popleft() # layer 1 pop gate cells
                grid[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1            




        