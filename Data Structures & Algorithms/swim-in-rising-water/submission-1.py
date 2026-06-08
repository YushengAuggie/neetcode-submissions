import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        Let's try Dijkstra algorithom
        """
        MAX_VAL = 2500
        queue = [(grid[0][0], (0, 0))]
        heapq.heapify(queue)
        N = len(grid)
        M = len(grid[0])
        visited = set()

        
        while queue:
            cur_closet_distance, cur_closet_node = heapq.heappop(queue)
            i, j = cur_closet_node

            if (i, j) in visited:
                continue

            visited.add((i, j))


            if i == N - 1 and j == M - 1:
                return cur_closet_distance
            
            # go through its neighbors
            # we need to make sure we do not revisit the same neighbor
            # go to other directions:
            for next_i, next_j in (
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
            ):
                if (
                    (next_i, next_j) in visited
                ) or (
                    next_i < 0 or next_j < 0
                    or next_i == N or next_j == M
                ):
                    continue
                
                heapq.heappush(
                    queue,
                    (max(grid[next_i][next_j], cur_closet_distance), (next_i, next_j))
                )
        return 0
                

                
            