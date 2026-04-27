class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        DP

        time: O(2^n) -> O(n)
        space: O(n)
        """

        mem = {}
        def dp(idx: int) -> int:
            """
            min cost from idx
            """
            if idx >= len(cost):
                return 0
            if idx in mem:
                return mem[idx]
            
            mem[idx] = cost[idx] + min(dp(idx + 1), dp(idx + 2))
            return mem[idx]
        
        return min(dp(0), dp(1))
