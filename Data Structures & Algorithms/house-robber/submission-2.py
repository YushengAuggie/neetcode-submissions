class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_vals = {}
        def dp(i: int) -> int:
            """
            How much it would be the largest if get to i
            no necessarily need to pick it
            time: O(n)
            space: O(n)
            """
            if i < 0:
                return 0
            if i in rob_vals:
                return rob_vals[i]
            rob_vals[i] = max(
                nums[i] + dp(i - 2),
                dp(i - 1)
            )
            return rob_vals[i]
        return dp(len(nums) - 1)
