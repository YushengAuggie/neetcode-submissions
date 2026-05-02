class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        This is a typical DP problem. 
        Let's solve this by considering that for every node,
         we can either choose to buy or not buy.

        The tricky part is if we choose to buy, 
        then we will not be able to buy again on the same day. 
        We have to sell it before we buy another one,
        so we need a way to specify whether we can buy or not.

        We can start by writing a DP first and then see how to optimize it.

        time: O(2^n) -> with mem -> O(n)
        space: O(n) -> O(n)

        """
        mem = {}

        def dp(
            idx: int, has_coin:bool = False, in_count_down:bool = False
        ) -> int:
            if (idx, has_coin, in_count_down) in mem:
                return mem[(idx, has_coin, in_count_down)]
            if idx == len(prices):
                return 0


            if has_coin:
                sell_profit = 0
                not_sell_profit = 0
                # If we have coin, 
                # the only option we can do is to 
                # sell it or not sell it.
                sell_profit = prices[idx] + dp(idx + 1, False, True)
                not_sell_profit = dp(idx + 1, True, False)

                mem[(idx, has_coin, in_count_down)] = max(sell_profit, not_sell_profit)
            else:
                buy_profit = 0
                skip_profit = 0

                if not in_count_down:
                    buy_profit = -prices[idx] + dp(idx + 1, True, False)
                not_sell_profit = dp(idx + 1, False, False)
                mem[(idx, has_coin, in_count_down)] = max(buy_profit, not_sell_profit)

            return mem[((idx, has_coin, in_count_down))]
        return dp(0)

