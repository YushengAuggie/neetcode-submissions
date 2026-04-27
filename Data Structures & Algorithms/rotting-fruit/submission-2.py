from collections import defaultdict
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Multi-source BFS
        every time enqueue the new rotten fruit
        Time: O(n*m)
        Space: O(n*m)
        """

        time = 0
        queue = []
        total_count = 0
        
        # enqueue rotten fruits
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    total_count += 1
                elif grid[i][j] == 1:
                    total_count += 1

        while queue:
            next_queue = []
            while queue:
                cur_i, cur_j = queue.pop()
                total_count -= 1

                for next_i, next_j in [
                    (cur_i + 1, cur_j),
                    (cur_i - 1, cur_j),
                    (cur_i, cur_j + 1),
                    (cur_i, cur_j - 1),
                ]:
                    if (
                        next_i < 0 or next_j < 0
                        or next_i == len(grid)
                        or next_j == len(grid[0])
                    ):
                        continue
                    elif grid[next_i][next_j] == 1:
                        grid[next_i][next_j] = 2
                        next_queue.append((next_i, next_j))
            if next_queue:
                queue = next_queue
                time += 1
        return time if total_count == 0 else -1

       
