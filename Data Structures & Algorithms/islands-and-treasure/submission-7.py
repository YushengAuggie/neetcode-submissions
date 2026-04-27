class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        start from the 0 and update fields around it
        time: O((n*m))
        space: O(n*m)
        """

        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))

        visited = set()
        step = 0
        while queue:
            next_queue = []
            while queue:
                cur_i, cur_j = queue.pop()
                visited.add((cur_i, cur_j))

                cur_val = grid[cur_i][cur_j]
                if cur_val == -1:
                    continue
                
                if step > cur_val:
                    continue
                else:
                    grid[cur_i][cur_j] = step

                for next_i, next_j in [
                    (cur_i + 1, cur_j),
                    (cur_i - 1, cur_j),
                    (cur_i, cur_j + 1),
                    (cur_i, cur_j - 1),
                ]:
                    if (
                        (next_i, next_j) in visited
                        or next_i < 0 or next_j < 0
                        or next_i == len(grid)
                        or next_j == len(grid[0])
                        or grid[next_i][next_j] == 0
                        or grid[next_i][next_j] == -1
                    ):
                        continue
                    next_queue.append((next_i, next_j))
            step += 1
            queue = next_queue