class Solution:

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        if l > r:
            return -1

        while l <= r:
            mid = r-l//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1   

        return -1      



    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            # Iterate row[0] -> [0][0] [0][1] [0][2]...[0][n]
            # perform binary search on that row
            nums = matrix[i][0:len(matrix[i])]
            if self.search(nums, target) > -1:
                return True

        return False        








          