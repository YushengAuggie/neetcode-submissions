class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(base: float, power: int) -> float:
            if base == 0:
                return 0
            if power == 0:
                return 1
            
            res = helper(base * base, power // 2)
            res = base * res if power % 2 else res
            return res
        
        res = helper(x, abs(n))
        return res if n > 0 else 1/res

