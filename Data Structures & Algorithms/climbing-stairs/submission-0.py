class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 0:
            return 0
        # f(n) = f(n-1) + f(n-2)
        ways = 0
        prev = 1
        prev_two = 0
        for i in range(1, n + 1):
            ways = prev + prev_two
            prev_two = prev
            prev = ways
        return ways