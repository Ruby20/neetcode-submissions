class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # reassign k
        k = len(nums) - k
        # quick select 
        l = 0
        r = len(nums) - 1
        def quickSelect(l, r):
            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    # swap p and i
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            # swap partition element with pivot
            nums[p], nums[r] = nums[r], nums[p]

            if k < p:
                return quickSelect(l, p - 1)        
            elif k > p:
                return quickSelect(p + 1, r)
            else:
                return nums[p]
        return quickSelect(l, r)        

