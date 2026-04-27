from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
            if count[n] == 2:
                return True
        return False
        