class Solution:
    def isHappy(self, n: int) -> bool:

        def breakSum(num: int) -> int:
            res = 0
            while num > 0:
                digit = num % 10
                res += digit ** 2
                num = num // 10
            return res
            
        fast = breakSum(n)
        slow = n
        
        while fast != slow:
            fast = breakSum(fast)
            fast = breakSum(fast)
            slow = breakSum(slow)
        return True if fast == 1 else False
    