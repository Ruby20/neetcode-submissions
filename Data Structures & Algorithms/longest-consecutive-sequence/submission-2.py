class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i, n in enumerate(nums):
            if n - 1 not in numSet:
                cur_len = 0
                while n + cur_len in numSet:
                    cur_len += 1
                longest = max(longest, cur_len)    
        return longest    

