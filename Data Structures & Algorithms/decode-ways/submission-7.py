from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        dp[i] -> on i how many options

        current either s[i + 1] or s[i]
        and ways 
        pick i:
        get s[i:i+1] helper(s[i+1:])
        get s[i:i+2] helper(s[i+2:])
        find all i, j in s and 
        """

        def helper(i: int) -> int:
            if i == len(s):
                return 1

            if s[i] == "0":
                return 0

            if i == len(s) - 1:
                return 1

            res = 0
            # choose two digits
            int_next = int(s[i: i + 2])
            if 10 <= int_next <= 26:
                res += helper(i + 2)
            
            # choose one digit
            res += helper(i + 1)

            return res
        
        return helper(0)
