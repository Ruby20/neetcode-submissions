class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # dims
        rows, cols = len(board), len(board[0])

        # visit the borders and mark all 0's as t (unsurrounded region)
        # this needs dfs helper func
        def capture(r, c):
            # out of bounds check
            if (min(r, c) < 0 or 
                r == rows or c == cols or
                board[r][c] != 'O'):
                    return

            board[r][c] = 'T'
            capture(r + 1, c)        
            capture(r - 1, c)        
            capture(r, c - 1)        
            capture(r, c + 1)        

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r in [0, rows - 1] or c in [0, cols - 1]):
                    capture(r, c)    

        # traverse the 2D arr to mark all the surrounded 0's as X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # traverse the 2D arr to mark all the unsurrounded t's to 0's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

        