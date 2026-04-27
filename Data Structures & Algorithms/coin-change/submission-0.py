class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        The problem with dp:
        for amount:
            what do we choose 
            dp[amount] = smallest can choose
        time: O(m*amount), m is len(coins)
        space: O(n) n = amount
        """
        mem = {}
        def helper(target:int) -> int:
            if target in mem:
                return mem[target]
            
            if target == 0:
                mem[target] = 0
                return 0

            min_count = amount + 1
            for coin in coins:
                if coin <= target:
                    count = 1 + helper(target - coin)
                    if min_count > count:
                        min_count = count
            mem[target] = min_count
            return mem[target]
        
        count = helper(amount)
        if count == amount + 1:
            return -1
        return count

