from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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


