class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        time: O(n^2) n * (n - 1) pairs of possibilities
        space: O(n)
        """

        mem = {}

        def helper(i: int, smallest_idx:int) -> int:
            if i == -1:
                return 0
            
            if (i, smallest_idx) in mem:
                return mem[(i, smallest_idx)]
            
            choose_i = 0
            if smallest_idx == -1 or nums[i] < nums[smallest_idx]:
                choose_i = 1 + helper(i - 1, i)
            skip_i = helper(i - 1, smallest_idx)
            mem[(i, smallest_idx)] = max(choose_i, skip_i)
            return mem[(i, smallest_idx)]
        return helper(len(nums) - 1, -1) 
            
                

        