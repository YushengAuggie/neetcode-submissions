class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        time: O(n * amount)
        space: O(amount)
        """
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]
        return dp[amount]
