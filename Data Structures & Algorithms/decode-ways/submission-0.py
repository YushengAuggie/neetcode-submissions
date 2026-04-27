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
        @lru_cache(None)
        def helper(i) -> int:
            """how many choices from s[i]"""
            if i >= len(s):
                return 1
            
            if s[i] == "0":
                return 0
            print(i, s[i])

            if i == len(s) - 1:
                return 1

            if s[i] == "1" or (
                s[i] == "2" and 0 <= int(s[i + 1]) <= 6
            ):  
                print("TWO ")
                return helper(i + 1) + helper(i + 2)


            print(s[i])
            return helper(i + 1)
        
        return helper(0)
