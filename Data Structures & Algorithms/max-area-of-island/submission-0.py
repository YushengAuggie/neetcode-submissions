class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        dfs
        time: O(n*m) size of the grid
        space: O(n*m) visited
        """
        def get_island_size(i:int, j:int) -> int:
            """Return the size of the island."""
            if (i, j) in visited or (
                i == len(grid) or j == len(grid[0])
            ) or (
                i < 0 or j < 0
            ) or grid[i][j] == 0:
                return 0

            res = 1
            visited.add((i, j))
            for next_i, next_j in [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
            ]:
                res += get_island_size(next_i, next_j)
            return res


        visited = set()
        max_size = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_size = max(get_island_size(i,j), max_size)
        return max_size