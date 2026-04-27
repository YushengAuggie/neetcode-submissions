import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cost = 0
        total_points = len(points)

        visited = set()
        pq = [(0, points[0][0], points[0][1])]
        heapq.heapify(pq)

        while pq and len(visited) < total_points:
            cur_cost, x, y = heapq.heappop(pq)
            if (x, y) in visited:
                continue
            cost += cur_cost
            visited.add((x, y))
            for x1, y1 in points:
                if (x1, y1) not in visited:
                    distance = abs(x - x1) + abs(y - y1)
                    heapq.heappush(
                        pq,
                        (
                            distance, x1, y1
                        )
                    )
        return cost




