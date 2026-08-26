class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # brute force approach - we maintain a new list
        # two pointers - we do it in place
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k        
