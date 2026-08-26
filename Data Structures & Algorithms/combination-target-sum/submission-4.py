class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        res = []

        def helper(i, total):
            if  i == len(nums) and total == target:
                res.append(combs[:])
                return
            if i >= len(nums) or total > target:
                return
            combs.append(nums[i])
            helper(i, total + nums[i])
            combs.pop()

            helper(i + 1, total)

        helper(0, 0)
        return res    

                