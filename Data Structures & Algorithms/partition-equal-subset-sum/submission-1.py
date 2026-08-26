class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        memo = {}
        def backtrack(i, target):
            if (i, target) in memo:
                return memo[(i, target)]

            if target == 0:
                return True    

            if i >= len(nums) or target < 0:
                return False
            
            memo[(i, target)] = backtrack(i + 1, target) or backtrack(i + 1, target - nums[i])

            return memo[(i, target)]

        return backtrack(0, sum(nums) // 2)    


        