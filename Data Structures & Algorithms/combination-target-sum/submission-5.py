class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combs = []
        nums.sort()

        def helper(i, total):
            if  total == target:
                res.append(combs[:])
                return
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                combs.append(nums[j])
                helper(j, total + nums[j])
                combs.pop()    

        helper(0, 0)
        return res    

                