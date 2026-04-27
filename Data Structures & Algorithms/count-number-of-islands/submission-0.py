class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Go through the whole grid, and update the number of islands + 1, and then goting to all
        directions and mark all neighbors as 0. 
        so in this case we do not need extra too much space.
        time: O(n) n is the elements in this grid
        space: O(1)

        """

        count_islands = 0

        def dfs(i:int, j:int, new_island:True) -> None:
            nonlocal count_islands

            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
                return
            
            
            if grid[i][j] == "1":
                if new_island:
                    count_islands += 1
                    new_island = False
                grid[i][j] = 0

                for row, col in (
                    (i + 1, j),
                    (i - 1, j),
                    (i, j + 1),
                    (i, j - 1),
                ):
                    dfs(row, col, new_island)
            return
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dfs(i, j, True)

        return count_islands