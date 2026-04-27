class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Brute force:
            try buying every step and selling in another step after that. 
            n^2 time complexity

        let's think about a better solution

        """

        max_revenue = 0
        for i, buy in enumerate(prices):
            for j in range(i + 1, len(prices)):
                max_revenue = max(
                    prices[j] - buy, max_revenue
                )
        return max_revenue
