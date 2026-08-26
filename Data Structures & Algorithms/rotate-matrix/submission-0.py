class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # two pointers
        left = 0
        right = len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top = left
                bottom = right

                # keep moving clockwise 
                # save top left
                topL = matrix[top][left + i]

                # move bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # move bottom right to bottom left
                matrix[bottom - i] [left] = matrix[bottom][right - i]
                
                # move top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # save top left in top right
                matrix[top + i][right] = topL

            left += 1
            right -= 1    
