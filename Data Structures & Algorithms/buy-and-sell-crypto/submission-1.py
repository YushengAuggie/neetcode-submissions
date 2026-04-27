class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Brute force:
            try buying every step and selling in another step after that. 
            n^2 time complexity

        let's think about a better solution:
            we can have two iterations:
            first: we get the data: the lowest value before this idx.
            second: we can check the current val - the lowest value to get the gain
                   and thus we can get the highest gain
            it would be O(n) time and O(n) space
        
        a even better solution with a lower space complexity
        we only iterate the array once
        and save the lowest point before this, and at the same time we calculate the
         current revenue if we sell it at the current index. thus we can get the max revent.

         O(n) time and O(1) space
        """

        # max_revenue = 0
        # for i, buy in enumerate(prices):
        #     for j in range(i + 1, len(prices)):
        #         max_revenue = max(
        #             prices[j] - buy, max_revenue
        #         )
        # return max_revenue

        if not prices or len(prices) < 2:
            return 0

        max_gain = 0
        lowest_val = prices[0]
        for idx in range(1, len(prices)):
            max_gain = max(prices[idx] - lowest_val, max_gain)
            lowest_val = min(lowest_val, prices[idx])
        return max_gain

