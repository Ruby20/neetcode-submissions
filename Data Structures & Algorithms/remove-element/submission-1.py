class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # brute force
        # remove the val and collect all the remaining into a new list

    #     res = []
    #     for i in range(len(nums)):
    #         if nums[i] != val:
    #             res.append(nums[i])

    #     # update the nums array since we the ouput needs to modify the original input
    #     for i in range(len(res)):
    #         nums[i] = res[i]

    #     return len(res)
    # # Time: O(n)
    # # Space :O(n)    
    # Two Pointer technique is optimal
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k        




