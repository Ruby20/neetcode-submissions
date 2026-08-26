class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
       # space optimized
        first, second = 1, 1

        for _ in range(n - 1):     
            temp = first
            first = first + second
            second = temp
        return first


        