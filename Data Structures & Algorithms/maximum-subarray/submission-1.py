class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's one pass algorithm
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            print(curSum, maxSum)
            maxSum = max(maxSum, curSum)

        return maxSum    
