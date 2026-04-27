class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        We can do a BFS for every individual cell in the array
        and see the first step it is able to reach the treasure;
        that value should be filled in the array.

        For the time complexity, in the worst case, for every cell we need to traverse all the other cells. So that would be (N × M)².

        For space, currently my idea is still to have another N × N array. We can think about how to optimize it later.
        """

        INF = int(math.pow(2, 31) - 1)

        def get_disctance(i: int, j: int) -> int:

            queue = [(i, j)]
            step = 0
            visited = set()

            while queue:
                next_queue = []

                while queue:
                    cur_i, cur_j = queue.pop()
                    visited.add((cur_i, cur_j))
                    if grid[cur_i][cur_j] == 0:
                        return step

                    for next_i, next_j in [
                        (cur_i + 1, cur_j),
                        (cur_i - 1, cur_j),
                        (cur_i, cur_j + 1),
                        (cur_i, cur_j - 1),
                    ]:
                        if (
                            (next_i, next_j) in visited
                            or next_i < 0
                            or next_j < 0
                            or next_i == len(grid)
                            or next_j == len(grid[0])
                            or grid[next_i][next_j] == -1
                        ):
                            continue
                        next_queue.append((next_i, next_j))

                queue = next_queue
                step += 1

            return INF

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == INF:
                    grid[i][j] = get_disctance(i, j)
        return
