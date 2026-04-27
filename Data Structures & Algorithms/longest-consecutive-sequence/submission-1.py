from collections import defaultdict
class Solution:
    def longestConsecutive_sol1(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                # num is the start of the list
                length = 1
                while num + length in nums_set:
                    length += 1
                max_len = max(length, max_len)
        return max_len

    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        dict_sequence_len = defaultdict(int)
        for num in nums:
            # 2, 3, 4, 5
            # 5, 6, 7
            if not dict_sequence_len[num]:
                dict_sequence_len[num] = dict_sequence_len[num - 1] + dict_sequence_len[num + 1] + 1
                dict_sequence_len[num - dict_sequence_len[num - 1]] = dict_sequence_len[num]
                dict_sequence_len[num + dict_sequence_len[num + 1]] = dict_sequence_len[num]
                max_len = max(max_len, dict_sequence_len[num])
        return max_len