class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use a hashset
        uniq = set()

        for n in nums:
            if n in uniq:
                return n
            uniq.add(n)
        