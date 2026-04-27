from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return nums

        count_num = defaultdict(int)
        freq_num = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count_num[num] += 1
        
        # bucket 
        for num, count in count_num.items():
            freq_num[count].append(num)
        
        ret_list = []
        while len(ret_list) < k:
            for cur_nums in freq_num[::-1]:
                ret_list.extend(cur_nums)
        return ret_list[:k]
            






        