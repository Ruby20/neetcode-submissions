class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 or 2 steps at a time

        # base case
        if n <= 3:
            return n

        # suppose for n = 5, 1 step at 5 and 1 step from 4 to 5
        n1, n2 = 1, 1
        
        i = n
        for i in range(n-1):
            tmp = n1
            n1 = n1 + n2
            n2 = tmp
            
        return n1 





        