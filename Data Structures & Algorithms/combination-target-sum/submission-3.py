class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        comb = []

        def helper(i, cur, total):
            if total == target:
                comb.append(cur[:])
                return
            if i >= len(nums) or total > target:
                return
            cur.append(nums[i])    
            helper(i, cur, nums[i] + total)        
            cur.pop()
            helper(i + 1, cur, total)

        helper(0, [], 0)    
        return comb
        