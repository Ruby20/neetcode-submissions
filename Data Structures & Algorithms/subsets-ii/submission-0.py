class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # so that we can skip dups
        subsets = []
        curset = []

        def backtracking(i):
            if i >= len(nums):
                subsets.append(curset[:])
                return

            curset.append(nums[i])
            backtracking(i + 1)
            curset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1 # skip dups
            backtracking(i + 1)

        backtracking(0)
        return subsets        

        