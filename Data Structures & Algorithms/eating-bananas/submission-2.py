class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = 0

        while left <= right:
            mid = (left + right) // 2

            # calc ceil func
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i]/mid)
            if total <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res        


        