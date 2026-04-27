import heapq
class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_queue = []
        for x, y in points:
            # print(x, y)
            heapq.heappush(k_queue, (-x*x - y*y, [x, y]))
            if len(k_queue) > k:
                # print("pop")
                heapq.heappop(k_queue)
            # print(k_queue)
            # print()
        return [point for _, point in k_queue]