class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Brute force:
        chose first ->
        not chose first -> 
        time: O(n)
        space: O(n)
        """
        # chose 0
        # so we start with the 3rd one and we cannot chose the last one
        max_vals = {}
        def dfs(cur:int, end:int) -> int:
            if cur > end:
                return 0
            if cur in max_vals:
                return max_vals[cur]
            
            # chose cur
            max_val = max(
                nums[cur] + dfs(cur + 2, end),
                dfs(cur + 1, end)
            )
            max_vals[cur] = max_val
            return max_val
        
        chose_0 = nums[0] + dfs(2, len(nums) - 2)
        max_vals = {}
        skip_0 = dfs(1, len(nums) - 1)
        return max(chose_0, skip_0)

            
