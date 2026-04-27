import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-i for i in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            max0 = -heapq.heappop(max_heap)
            max1 = -heapq.heappop(max_heap)
            if max0 != max1:
                diff = max0 - max1
                heapq.heappush(max_heap, -diff)
            
        return -max_heap[0] if max_heap else 0


        