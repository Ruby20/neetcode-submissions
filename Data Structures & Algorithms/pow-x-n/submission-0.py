class Solution:
    def myPow(self, x: float, n: int) -> float:
        # base case
        # x ^ 0 = 1
        # x == 0 return 0
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = helper(x , n // 2)
            res = res * res

            return x * res if n % 2 else res
        power = helper(x, abs(n)) 
        return  power if n >= 0 else 1 / power
