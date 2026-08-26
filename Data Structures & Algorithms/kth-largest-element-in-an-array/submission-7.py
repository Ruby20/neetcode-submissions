class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k # kth index from the end

        def quickSelect(l, r):
            pivot = nums[r]
            p = l # partition

            # find the partition index where elem on the left < elem on right
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            # swap the pivot with the partition index
            nums[p], nums[r] = nums[r], nums[p]

            if k < p:
                # run quick select on the left portion
                return quickSelect(l, p - 1)
            elif k > p:
                return quickSelect(p + 1, r)
            else: # p == k
                return nums[p]


        return quickSelect(0, len(nums) - 1)    
