class Solution:
    def climbStairs(self, n: int) -> int:
        # two pointers to track the ways
        one = 1
        two = 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one    
        