class Solution:
    def reverse(self, x: int) -> int:
        positive = True
        if x < 0:
            positive = False
            x = abs(x)
        reversed_int = 0

        uppder_bound = math.pow(2, 31) - 1
        lower_bound = math.pow(2, 31)

        while x:
            cur = x % 10
            x = x // 10
            reversed_int = reversed_int * 10 + cur 
            if positive and reversed_int > uppder_bound:
                return 0
            elif not positive and reversed_int > lower_bound:
                return 0

        return reversed_int if positive else -reversed_int
        
        