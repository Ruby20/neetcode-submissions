class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # get dims
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(i, r, c):
            if  i == len(word):
                return True

            if (min(r, c) < 0 or 
                r >= rows or c >= cols or
                (r, c) in visit or
                board[r][c] != word[i]):
                    return False

            visit.add((r, c))        

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            res = (dfs(i + 1, r + 1, c) or
                  dfs(i + 1, r - 1, c) or  
                  dfs(i + 1, r, c + 1) or
                  dfs(i + 1,r, c - 1))

            visit.remove((r, c))
            return res

        for row in range(rows):
            for col in range(cols):
                if dfs(0, row, col):
                    return True
        return False                          
            

        