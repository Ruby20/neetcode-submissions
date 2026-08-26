class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # solve using two pointers
        l = 0 
        n = len(numbers)
        r = n-1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r+ 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else :
                l += 1




        
