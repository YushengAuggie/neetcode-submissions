class Solution:
    def climbStairs(self, n: int) -> int:
        visited = {
            0:0,
            1:1,
            2:2,
        }
        def dfs(i) -> int:
            if i in visited:
                return visited[i]
            visited[i] = dfs(i - 1) + dfs(i - 2)
            return visited[i]
        return dfs(n)