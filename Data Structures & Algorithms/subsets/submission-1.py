class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        curset = []    
        def backtracking(i):
            # base case
            if i >= len(nums):
                subsets.append(curset[:])
                return

            curset.append(nums[i])    
            backtracking(i + 1)
            curset.pop()

            backtracking(i + 1)
            
        backtracking(0)
        return subsets    
        