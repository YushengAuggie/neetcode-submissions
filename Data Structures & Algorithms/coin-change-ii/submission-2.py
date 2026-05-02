class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        we can use DB to do this

        try every element, pick / not pick 
        and the next is to try all elements >= it, pick / not pick
        if the last did not pick, then we can skip the same value again

        and it is O(2^n) time and O(n) space
        and then we add mem table
        time: O(n * amount)
        space: O(n * amount)

        """

        mem = {}
        def dp(idx:int, target: int) -> int:
            if target == 0:
                return 1

            if (idx, target) in mem:
                return mem[(idx, target)]
                
            if target < 0:
                return 0
            
            if idx == len(coins):
                return 0
            
            # skip
            skip = dp(idx + 1, target)

            # pick 
            target -= coins[idx]
            pick = dp(idx, target)
            target += coins[idx]

            mem[(idx, target)] = skip + pick
            return mem[(idx, target)]

        return dp(0, amount)
            
            


