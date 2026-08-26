class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevrow = [0] * n
       
        for r in range(m-1, -1, -1): # bottom right
           currow = [0] * n # assign the cur row
           currow[n-1] = 1 # assign the last col to 1(our price)
           for c in range(n-2, -1, -1):
              currow[c] = currow[c+1] + prevrow[c] # look right + bottom
           prevrow = currow   
              
        return prevrow[0]      
                

        