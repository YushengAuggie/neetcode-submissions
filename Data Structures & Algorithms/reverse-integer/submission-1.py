import math
class Solution:
    def reverse(self, x: int) -> int:
        positive = True
        if x < 0:
            positive = False
            x = -x
        reversed_num = int(str(x)[::-1])
        if reversed_num > math.pow(2, 31) - 1:
            return 0
        return reversed_num if positive else -reversed_num
