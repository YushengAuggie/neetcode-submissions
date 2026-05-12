class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        ret = 1
        positive_power = True
        if n < 0:
            n = -n
            positive_power = False
        while n:
            ret *= x 
            n -= 1
            
        return ret if positive_power else 1/ret