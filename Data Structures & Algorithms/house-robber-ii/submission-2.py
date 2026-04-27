class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        
        def helper(start:int, end:int) -> int:
            prev_max = 0 # the previous one was skipped
            cur_max = 0 # choose the current one
            max_val = 0
            for i in range(start, end + 1):
                dummy = cur_max 
                cur_max = max(nums[i] + prev_max, cur_max)
                prev_max = dummy
            return max(prev_max, cur_max)
        if len(nums) == 1:
            return nums[0]
        chose_0 = helper(0, len(nums) - 2)
        skip_0 = helper(1, len(nums) - 1)
        return max(chose_0, skip_0)



        