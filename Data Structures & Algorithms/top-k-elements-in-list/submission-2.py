from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return nums

        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1

        
        heap_num_count = []
        for num, count in num_count.items():
            heapq.heappush_max(heap_num_count, (count, num))
        
        ret_list = []
        while len(ret_list) < k:
            count, num = heapq.heappop_max(heap_num_count)
            ret_list.append(num)
        return ret_list



        