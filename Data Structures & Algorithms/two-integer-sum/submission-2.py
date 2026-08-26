class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # quickly identify pairs/indices that sum up to target
        # 1.brute force brute force method
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    break

        return res