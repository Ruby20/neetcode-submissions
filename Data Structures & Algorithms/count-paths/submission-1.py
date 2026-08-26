class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # draw an extra cols of 0's 
        # assign 1 to the bottom right and start adding bottom + right cells
        prevRow = [0] * n
        
        for r in range(m-1, -1, -1):
            curRow = [0]* n
            curRow[n-1] = 1
            for c in range(n-2, -1, -1):
                curRow[c] = curRow[c+1] + prevRow[c]
            prevRow = curRow

        return prevRow[0]         
             
        