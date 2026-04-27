class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        up = [1] * n
        for i in range(m):
            left = 1
            for j in range(n):
                if j == 0 or i == 0:
                    up[j] = 1
                else:
                    cur = left + up[j]
                    left = cur
                    up[j] = cur
            print(up)
        return up[n-1]