class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        bottom up dp
        time: O(n^2)
        space: O(n)
        """
        n = len(nums)
        dp = [float("inf")] * n
        dp[-1] = 0

        for idx in range(n - 2, -1, -1):
            for nxt in range(
                idx + 1, min(n, idx + nums[idx] + 1)
            ):
                dp[idx] = min(dp[idx], 1 + dp[nxt])
                
        return dp[0]