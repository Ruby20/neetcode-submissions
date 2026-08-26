class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sum_squares(n):
            square_sum = 0
            
            while n:
                digit = n % 10
                digit = digit**2
                square_sum += digit
                n = n // 10
            return square_sum

        visit = set()    
        while n not in visit:
            visit.add(n)
            n = sum_squares(n)
            if n == 1:
                return True
        return False    
