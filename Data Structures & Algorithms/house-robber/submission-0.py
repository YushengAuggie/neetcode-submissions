class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        pick this one or skip
            pick -> i + 1
            skip -> i
        dp

        2 branch 2 branch 2 
        time: 2^n
        space: O(n)
        dp dict[i] = val
        if we get to i, the max value we can get
        no matter choose i or not
        """
        max_val_step = {}
        def dp(i:int) -> int:
            """If we get to i, the max val we can get."""
            if i >= len(nums):
                return 0
            
            if i in max_val_step:
                return max_val_step[i]

            # choose i
            choose_max_val = nums[i] + dp(i + 2)
            not_choose_max_val = dp(i + 1)
            max_val_step[i] = max(choose_max_val, not_choose_max_val)
            return max_val_step[i]
        return dp(0)
         