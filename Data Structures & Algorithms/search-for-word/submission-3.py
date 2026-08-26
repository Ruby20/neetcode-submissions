class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # dfs with backtracking
        if not board or not board[0]:
            return False

        # get board dims
        rows = len(board)
        cols = len(board[0])

        visit = set()
        def dfs(i, r, c):
            # base cases
            if i == len(word):
                return True

            if (min(r, c) < 0 or     
              r >= rows or c >= cols or
              word[i] != board[r][c] or
              (r, c) in visit):
                return False

            visit.add((r, c)) 
            res = (dfs(i + 1, r + 1, c) or
                  dfs(i + 1, r - 1, c) or
                  dfs(i + 1, r, c + 1)  or
                  dfs(i + 1, r , c - 1) )   
            visit.remove((r, c))      
            return res      

        for r in range(rows):
            for c in range(cols):
                if dfs(0, r, c):
                    return True
        return False        







        