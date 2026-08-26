class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        # we need to sort the array to remove dup
        nums.sort()
        
        # a + b + c == 0
        for i in range(n):
            a = nums[i]

            if i > 0 and nums[i-1] == a: # check for duplicates
                continue
            # initialize the l and r 
            l = i + 1
            r = n - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a,nums[l], nums[r]])           
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res            



        