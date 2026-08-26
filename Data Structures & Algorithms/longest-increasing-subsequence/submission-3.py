class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # using DP
        LIS = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            # print("i", i, nums[i])
            for j in range(i+1, len(nums)):
                # print("j", j, nums[j])
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)
