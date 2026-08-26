class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in nums:
            # check if start of a sequence? has no left neighbor
            if n-1 not in numset:
                cur = 0
                while (n + cur) in numset:
                    cur += 1
                    longest = max(longest, cur)
        return longest            

