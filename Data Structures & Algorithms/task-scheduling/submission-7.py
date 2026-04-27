import heapq
from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        q = deque()
        time = 0

        while max_heap or q:
            time += 1
            if max_heap:
                minor_cnt = heapq.heappop(max_heap)
                minor_cnt += 1
                if minor_cnt < 0:
                    q.append((minor_cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time
                

        