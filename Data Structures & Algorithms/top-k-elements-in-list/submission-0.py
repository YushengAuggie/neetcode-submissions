from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1
        
        num_occur_list = sorted([(k, v) for k,v in num_count.items()], key=lambda x: -x[1])
        return [num for num, occurance in num_occur_list[:k]]
        