class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i, n in enumerate(nums):
            cur_len = 0
            while n in numSet:
                cur_len += 1
                n = n + 1
            longest = max(longest, cur_len)    
        return longest    

