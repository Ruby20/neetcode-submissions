class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxval = max(piles)
        left = 1 
        right = maxval

        while left <= right:
            mid = (left + right) // 2
            total_time = 0
            for i in range(len(piles)):
                total_time += math.ceil(float(piles[i]) / mid )
            if total_time <= h:    
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res            

       

        
