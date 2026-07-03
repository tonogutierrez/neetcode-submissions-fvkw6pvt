class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        for divisor in [2,3,5]:
            while n % divisor == 0:
                n = n // divisor

        if n == 1:
            return True
        else:
            return False 