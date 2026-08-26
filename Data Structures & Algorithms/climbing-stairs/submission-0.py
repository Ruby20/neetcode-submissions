class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 or 2 steps at a time

        # base case
        if n <= 3:
            return n
        n1, n2 = 1, 1
        
        i = n
        for i in range(2, n+1)  :
            tmp = n1 + n2
            n1 = n2
            n2 = tmp
        return n2    





        