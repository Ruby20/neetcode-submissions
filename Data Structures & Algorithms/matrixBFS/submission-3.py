from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols =  len(grid[0])
        visit = set()
        que = deque()
        que.append((0,0))
        visit.add((0,0))

        length = 0

        while que:
            for i in range(len(que)):
                r,c = que.popleft()
                # check if we reached destination
                if r == rows - 1 and c == cols-1:
                    return length


                # get the neighbors
                directions = [[0, -1], [0, 1], [1, 0] ,[-1, 0]]

                for (dr,dc) in directions:
                    if (min(r + dr,c + dc) < 0 or 
                     r+dr == rows or c+dc == cols
                     or grid[r+dr][c+dc] == 1 or (r+dr,c+dc) in visit):
                        continue
                    que.append((r+dr, c+dc)) 
                    visit.add((r+dr, c+dc)) 
            length += 1 
        return -1             
                     


