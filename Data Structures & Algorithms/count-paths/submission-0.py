class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        """
        mem = {}

        def dp(i:int, j:int) -> int:
            if (i, j) in mem:
                return mem[(i, j)]
            if i == -1 or j == -1:
                return 0
            if i == 0 and j == 0:
                return 1
            mem[(i, j)] = dp(i - 1, j)
            mem[(i, j)] += dp(i, j - 1)
            return mem[(i, j)]
        print(mem)
        return dp(m - 1, n - 1)
        