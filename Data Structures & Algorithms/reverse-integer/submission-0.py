import math
class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x = -x
        reversed_num = int(str(x)[::-1])
        print(reversed_num, math.pow(2, 31) - 1, reversed_num > math.pow(2, 31) - 1)
        if reversed_num > math.pow(2, 31) - 1:
            return 0
        return -reversed_num if negative else reversed_num
