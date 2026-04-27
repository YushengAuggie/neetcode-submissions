import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        time: O(n^2)
        space: O(n^2)
        """
        n = len(points)
        dist = [float("inf") for _ in range(n)]
        visited = [False for _ in range(n)]
        dist[0] = 0
        count = 0
        res = 0

        while count < n:
            node_idx = -1

            # current unvisited smallest dist
            for i in range(n):
                if not visited[i] and (
                    node_idx == -1 or dist[node_idx] > dist[i]
                ):
                    node_idx = i
            
            # print("node_idx", node_idx)
            # add the edge to this node
            visited[node_idx] = True
            count += 1
            res += int(dist[node_idx])
            # print(dist)
            # print("res", res)
            # print("")

            # update dist with this node
            for i in range(n):
                if i == node_idx:
                    continue
                x1, y1 = points[node_idx]
                x2, y2 = points[i]
                distance = abs(x1 - x2) + abs(y1 - y2)
                dist[i] = min(distance, dist[i])
            
        return res



                



